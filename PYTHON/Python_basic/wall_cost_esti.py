import math
def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    cost = math.ceil(((sqft_walls+sqft_ceiling)/sqft_per_gallon )) * cost_per_gallon
    return cost

project_cost = get_cost(432,144,400,15) 
print(project_cost)