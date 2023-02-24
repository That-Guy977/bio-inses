import sys, os, json
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
from simulation import *
from simulation.entity import *

BASE_DIR = sys.argv[1]

screen, (entities, pests, preds, traps), seed = init(None, BASE_DIR)
clk = pygame.time.Clock()
data = {
  "seed": seed,
  "dur": 0,
  "dt": Entity.dt,
  "count": []
}
for t in range(util.tlimit):
  clk.tick()
  tick(screen, entities, lambda: print(json.dumps({ **data, "dur": t })))
  capture.save()
  data["count"].append((len(pests), len(preds), sum(map(len, Trap.traps))))
  if clk.get_time() > 10_000:
    Entity.log("MAIN", "ltnc")
    break
  check_end(pests, preds, traps, 50)
