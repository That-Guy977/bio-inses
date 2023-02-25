import sys, os, json
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
from simulation import *
from simulation.entity import *

BASE_DIR = sys.argv[1]

screen, entities, seed = init(None, BASE_DIR)
clk = pygame.time.Clock()
data = {
  "seed": seed,
  "dur": 0,
  "dt": Entity.dt,
  "count": []
}
while True:
  clk.tick()
  tick(screen, entities, lambda: print(json.dumps({ **data, "dur": Entity.tick - 1 })))
  capture.save()
  data["count"].append(Insect.counts.copy())
  if clk.get_time() > 10_000:
    Entity.log("MAIN", "ltnc")
    break
  check_end(300)
