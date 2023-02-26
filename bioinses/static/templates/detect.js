function update(event) {
  const [file] = event.target.files;
  if (file) {
    loading();
    setTimeout(display, 2000);
  } else {
    document.getElementById("preview").textContent = "";
  }
}

function loading() {
  const loading = document.querySelector(".loading");
  loading.style.display = "block";
}

function display() {
  const preview = document.getElementById("preview");
  const loading = document.querySelector(".loading");
  loading.style.display = "none";
  preview.src = "/static/detect.jpg";
  const vals = document.getElementById("vals");
  vals.innerHTML = `
    <span style="font-size: 24px;">พบแมลง 102 ตัว</span>
    <span style="font-size: 24px; color: red;">พบแมลงไม่ดี 57 ตัว</span>
    <span style="font-size: 24px; color: blue;">พบแมลงดี 45 ตัว</span>
    <br>
    <button>รายละเอียด</button>
    <a class="flex" href="/simulation/">Simulation</a>
  `;
}
