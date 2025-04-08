from terrain import Terrain
import json

with open('/home/catnee/Procedural-Maps/src/default_world_config.json') as json_file:
    world_conf = json.load(json_file)

terrain = Terrain(config=world_conf, seed=1234, shape=[50,50])

print(terrain.get_biome_map())