import itertools


class FindDistance:
    """
    Класс для поиска минимального маршрута
    """
    COEF = 0.5
    DEGREE = 2

    def find_dictance(
            self,
            point_1,
            point_2,
    ):
        """
        Находит расстояние между двумя точками
        """
        return (
                    (point_2[0] - point_1[0]) ** self.DEGREE + (point_2[1] - point_1[1]) ** self.DEGREE  # noqa
        ) ** self.COEF

    # def find_count_routers(self, count_points):
    #     factorial = 1
    #
    #     for i in range(2, count_points):
    #         factorial *= i
    #     return factorial

    @staticmethod
    def find_all_combinations(
            intermed_points,
            start_point,
            end_point,
    ):
        """
        Находит все комбинации точек
        """
        result_gen = itertools.permutations(intermed_points)
        routers_list = []
        for router in result_gen:
            router = list(router)
            router.insert(0, *start_point)
            router.append(*end_point)
            routers_list.append(router)

        return routers_list

    def find_all_distance(
            self,
            intermed_points,
            start_point,
            end_point=None,
    ):
        """
        Находит расстояния всех возможных маршрутов
        """

        end_point = start_point if not end_point else end_point

        self.routers_list = self.find_all_combinations(
            intermed_points,
            start_point,
            end_point,
        )
        min_distance = float('inf')

        for router in self.routers_list:
            distance = 0
            num = len(router)
            index = 1
            while num > 0:
                try:
                    if index == 1:
                        point_1 = router[index - 1]
                        point_2 = router[index]
                        index += 1
                    else:
                        point_1 = router[index - 1]
                        point_2 = router[index + 1]
                        index += 2
                    distance += self.find_dictance(
                        point_1=point_1,
                        point_2=point_2,
                    )
                except IndexError:
                    pass
                router.insert(
                    index,
                    distance,
                )

                num -= 1

            if distance < min_distance:
                min_distance = distance
                min_router = router

        return min_router

    def print_min_router(
            self,
            intermed_points,
            start_point,
            end_point=None,
    ):
        """
        Выводит информацию о минимальном маршруте
        """

        min_router = self.find_all_distance(
            intermed_points=intermed_points,
            start_point=start_point,
            end_point=end_point,
        )

        len_router = len(min_router)

        # записываем в переменную начало строки
        string = f'{min_router[0]} -> {min_router[1]}[{min_router[2]}]'
        for index in range(2, len_router - 2, 2):
            string += f'-> {min_router[index + 1]}[{min_router[index + 2]}]'
        # записываем в переменную конец строки
        string += f'= {min_router[-1]}'

        # либо так, но у нас будет лишние условия,
        # будем крутить лишний раз цикл
        # и перезаписывать переменную string
        # string = ''
        # for index in range(0, len(min_router), 2):
        #     if index < 2:
        #         string += f'{min_router[index]} -> {min_router[index+1]}[{min_router[index+2]}]'  # noqa
        #     elif index == len(min_router) - 2:
        #         string += f'= {min_router[index+1]}'
        #     else:
        #         string += f'-> {min_router[index+1]}[{min_router[index+2]}]'

        print(string)


dict_points = {
    'Почтовое отделение': (0, 2),
    'Ул. Грибоедова, 104/25': (2, 5),
    'Ул. Бейкер стрит, 221б': (5, 2),
    'Ул. Большая Садовая, 302-бис': (6, 6),
    'Вечнозелёная Аллея, 742': (8, 3),
}

if __name__ == '__main__':
    values_points = list(dict_points.values())

    # отделяем начальную точку от остальных
    intermed_points = values_points[1:]
    start_point = values_points[:1]

    FindDistance().print_min_router(
        intermed_points=intermed_points,
        start_point=start_point,
    )
