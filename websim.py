import sys, os, json
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
from simulation import *
from simulation.entity import *

BASE_DIR = sys.argv[1]

screen, entities, seed = init(None, BASE_DIR)
meta = {
  "seed": seed,
  "tlimit": 300,
}
done = False
clk = pygame.time.Clock()

def main():
  out()
  while True:
    tick(screen, entities, finalize)
    out(Insect.counts)
    clk.tick()
    capture.save()
    if clk.get_time() > 10_000:
      Entity.log("MAIN", "ltnc")
      break
    check_end(meta["tlimit"])

def out(data = None):
  print(json.dumps({
    "dt": Entity.dt,
    "tick": Entity.tick,
    "done": done,
    "meta": meta,
    "data": data
  }))

def finalize():
  global done
  done = True
  out(Insect.count)

if __name__ == "__main__":
  main()
