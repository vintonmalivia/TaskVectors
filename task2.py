import pandas
import numpy
import matplotlib.pyplot as plt

amount_of_strings = 0
amount_of_numbers = 0
vectorsList = pandas.read_csv('vectors.csv', header=None).__array__(dtype=float)

def calc_euclidean_distance_between_all_pairs():
    """This function calculates the Euclidean distance between all pairs of distinct vectors in vectors.csv."""
    current_vector_index = 0
    second_current_vector_index = 1
    min_euclidean_distance = 0
    first_min_euclidean_distance_index = 0
    second_min_euclidean_distance_index = 0
    max_euclidean_distance = 0
    first_max_euclidean_distance_index = 0
    second_max_euclidean_distance_index = 0
    vectors_dictionary = {}
    amount_of_vector_pairs = 0
    while current_vector_index < len(vectorsList):
        while second_current_vector_index < len(vectorsList):
            if ((vectorsList[current_vector_index]) != (vectorsList[second_current_vector_index])).all():
                print(
                    'Euclidean distance for vectors under indices ' + str(current_vector_index) +
                    ' and ' + str(second_current_vector_index) + ':')
                print(numpy.linalg.norm(vectorsList[current_vector_index] - vectorsList[second_current_vector_index]))

                if round(numpy.linalg.norm(
                        vectorsList[current_vector_index] - vectorsList[second_current_vector_index]),
                        1) in vectors_dictionary:
                    vectors_dictionary[round(
                        numpy.linalg.norm(vectorsList[current_vector_index] - vectorsList[second_current_vector_index]),
                        1)] += 1
                else:
                    vectors_dictionary[round(
                        numpy.linalg.norm(vectorsList[current_vector_index] - vectorsList[second_current_vector_index]),
                        1)] = 1

                if min_euclidean_distance == 0 or min_euclidean_distance > numpy.linalg.norm(
                        vectorsList[current_vector_index]
                        - vectorsList[second_current_vector_index]):
                    """Calculating the minimum Euclidean distance"""
                    min_euclidean_distance = numpy.linalg.norm(vectorsList[current_vector_index] -
                                                               vectorsList[second_current_vector_index])
                    first_min_euclidean_distance_index = current_vector_index
                    second_min_euclidean_distance_index = second_current_vector_index
                if max_euclidean_distance < numpy.linalg.norm(vectorsList[current_vector_index] -
                                                              vectorsList[second_current_vector_index]):
                    """Calculating the maximum Euclidean distance"""
                    max_euclidean_distance = numpy.linalg.norm(vectorsList[current_vector_index] -
                                                               vectorsList[second_current_vector_index])
                    first_max_euclidean_distance_index = current_vector_index
                    second_max_euclidean_distance_index = second_current_vector_index
                amount_of_vector_pairs += 1
            second_current_vector_index += 1
        current_vector_index += 1
        second_current_vector_index = current_vector_index + 1
    print('\nThe minimum Euclidean distance got a pair of vectors with indices '
          + str(first_min_euclidean_distance_index) + ' and ' + str(second_min_euclidean_distance_index) + '. '
          'The value of the Euclidean distance for this pair of vectors is ' + str(min_euclidean_distance) + '.')
    print('\nThe maximum Euclidean distance got a pair of vectors with indices '
          + str(first_max_euclidean_distance_index) + ' and ' + str(second_max_euclidean_distance_index) + '. '
          'The value of the Euclidean distance for this pair of vectors is ' + str(max_euclidean_distance) + '.')

    print(amount_of_vector_pairs)
    plt.title('Distribution of Euclidean distances')
    plt.xlabel('Euclidean distance')
    plt.ylabel('Amount of pairs')
    plt.bar(vectors_dictionary.keys(), vectors_dictionary.values(), width=0.05, color='g')
    plt.show()


calc_euclidean_distance_between_all_pairs()
