import math
catalog_matrix = {
"SAMSUNG": [0.20, 0.30, 0.19],
"INFINIX": [0.60, 0.78, 0.45],
"ITEL": [0.45, 0.08, 0.56],
"OPPO": [0.61, 0.52, 0.80]
}
print(" Product recomender systems")
price = float(input("Enter your price preference (0.0-1.0): "))
tech_spec = float(input("Enter your tech spec(0.0-1.0): "))
life_span = float(input("Enter its lifespan(0.0-1.0):"))
user_vector = [price,tech_spec,life_span]
k = int(input("Enter number of recommendations you want: "))
calculated_distance_matrix = []  # Where to store results after calculations are done
for catalog_id in catalog_matrix:
    squared_sum_accumulator = 0.0
    for vector_index in range(len(user_vector)):
        delta = (user_vector[vector_index] - catalog_matrix[catalog_id][vector_index])
        squared_sum_accumulator += delta*delta
        final_distance = math.sqrt(squared_sum_accumulator)
        calculated_distance_matrix.append((catalog_id,final_distance))
        for i in range(len(calculated_distance_matrix)):
            for j in range(i +1, len(calculated_distance_matrix)):
                if calculated_distance_matrix[1][1] > calculated_distance_matrix[j][1]: # this is done in order to sort from the smallest to the laegest 
                    temp = calculated_distance_matrix[i]
                    calculated_distance_matrix[i] = calculated_distance_matrix[j]
                    calculated_distance_matrix[j] = temp
                    recommendations = calculated_distance_matrix[:k]
                    print("Recomendations")
                    print("Rank| ProductID| Distance")
                    rank = 1
                    for item in recommendations:
                        print(rank, "|", item[0], "|", round(item[1], 4))
                        rank += 1
                        print("Recommendation process complete")