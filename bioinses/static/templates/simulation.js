let run = null;
let data = []
let dur = -1;

let tick = 0;
let playing = false;
let repeating = false;

async function start() {
  document.getElementById("start").disabled = true;
  document.querySelector(".loading").style.display = "block";
  const info = await fetch("/websim/").then((res) => res.json());
  run = info.dt;
  dur = info.meta.tlimit;
  document.getElementById("start").style.display = "none";
  while (true) {
    const tickInfo = await fetch(`/websim/${run}/`).then((res) => res.json());
    if (tickInfo.done) {
      dur = tickInfo.tick - 1;
      break;
    }
    data.push(tickInfo.data);
    document.getElementById("load-progress").textContent = `(${tickInfo.tick}/${dur})`;
  }
  document.querySelector(".loading").style.display = "none";
  document.getElementById("load-progress").style.display = "none";
  document.getElementById("result").style.display = "flex";
  loadFrame();
}

function loadFrame() {
  document.getElementById("frame").src = `/media/runs/${run}/${tick.toString().padStart(4, "0")}.png`;
  document.getElementById("tick").textContent = `${tick}/${dur}`;
  updateControls();
}

function updateControls() {
  setEnabled("media-start", playing || tick !== 0);
  setEnabled("media-end", playing || tick !== dur);
  setEnabled("media-prev", !playing && tick !== 0);
  setEnabled("media-next", !playing && tick !== dur);
}

function playpause() {
  if (!playing) {
    play();
  } else {
    pause();
  }
  updateControls();
}

function play() {
  playing = true;
  document.getElementById("playpause-icon")
    .classList.replace("fa-play", "fa-pause");
  if (tick === dur) tick = -1;
  const playNext = () => {
    if (playing) {
      if (tick < dur || repeating) {
        tick++;
        if (tick > dur) tick = 0;
        loadFrame();
        setTimeout(playNext, 100);
      } else {
        pause();
        updateControls();
      }
    }
  }
  playNext();
}

function pause() {
  playing = false;
  document.getElementById("playpause-icon")
    .classList.replace("fa-pause", "fa-play");
}

function repeat() {
  repeating = !repeating;
  document.getElementById("repeat-icon").parentElement
    .classList.toggle("selected");
}

function prev() {
  tick--;
  if (tick < 0) tick = dur;
  pause();
  loadFrame();
}

function next() {
  tick++;
  if (tick > dur) tick = 0;
  pause();
  loadFrame();
}

function toStart() {
  tick = 0;
  pause();
  loadFrame();
}

function toEnd() {
  tick = dur;
  pause();
  loadFrame();
}

function setEnabled(id, enabled) {
  document.getElementById(id).disabled = !enabled;
}
