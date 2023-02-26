let data = null;
let tick = 0;
let playing = false;
let repeating = false;

async function start() {
  document.getElementById("start").disabled = true;
  document.querySelector(".loading").style.display = "block";
  data = await fetch("/websim/").then((res) => res.json());
  load();
}

function load() {
  document.querySelector(".loading").style.display = "none";
  document.getElementById("start").style.display = "none";
  document.getElementById("result").style.display = "flex";
  document.getElementById("controls").style.display = "flex";
  loadFrame();
}

function loadFrame() {
  document.getElementById("frame").src = `/media/runs/${data.dt}/${tick.toString().padStart(4, "0")}.png`;
  document.getElementById("clock").textContent = `${tick}/${data.dur}`;
}

function playpause() {
  if (!playing) {
    play();
  } else {
    pause();
  }
}

function play() {
  playing = true;
  document.getElementById("playpause")
    .classList.replace("fa-play", "fa-pause");
  if (tick === data.dur) tick = -1;
  const playNext = () => {
    if (playing) {
      if (tick < data.dur || repeating) {
        tick++;
        if (tick > data.dur) tick = 0;
        loadFrame();
        setTimeout(playNext, 100);
      } else pause();
    }
  }
  playNext();
}

function pause() {
  playing = false;
  document.getElementById("playpause")
    .classList.replace("fa-pause", "fa-play");
}

function repeat() {
  repeating = !repeating;
  document.getElementById("repeat").parentElement
    .classList.toggle("selected");
}

function prev() {
  tick--;
  if (tick < 0) tick = data.dur;
  pause();
  loadFrame();
}

function next() {
  tick++;
  if (tick > data.dur) tick = 0;
  pause();
  loadFrame();
}

function toStart() {
  tick = 0;
  pause();
  loadFrame();
}

function toEnd() {
  tick = data.dur;
  pause();
  loadFrame();
}
