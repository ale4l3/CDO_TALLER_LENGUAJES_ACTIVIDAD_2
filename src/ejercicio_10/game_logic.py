def run_game(rounds):
    # Se define el criterio del puntaje
    kill_point_value = 2
    assist_point_value = 1
    surviving_point_value = 5

    # Se recorre la lista, se accede al diccionario de cada ronda.
    total_stats = {
    'Shadow': {'kills': 0, 'assists': 0, 'deaths': 0, 'mvp': 0, 'points': 0},
    'Blaze': {'kills': 0, 'assists': 0, 'deaths': 0, 'mvp': 0, 'points': 0},
    'Viper': {'kills': 0, 'assists': 0, 'deaths': 0, 'mvp': 0, 'points': 0},
    'Frost': {'kills': 0, 'assists': 0, 'deaths': 0, 'mvp': 0, 'points': 0},
    'Reaper': {'kills': 0, 'assists': 0, 'deaths': 0, 'mvp': 0, 'points': 0}
    }
    round_points_initial = {
    'Shadow': 0,
    'Blaze': 0,
    'Viper': 0,
    'Frost': 0,
    'Reaper': 0
    }
    round_number = 0

    for round in rounds:
        round_number += 1
        round_points = round_points_initial.copy()
        points_round_mvp = 0
        player_round_mvp = 'zzz'
    # Se accede al diccionario de los jugadores.

        for player, round_stats_player in round.items():
            for stat_type, stat_value in round_stats_player.items():
                # Se suman los puntos dependiendo del tipo de la acción ronda por ronda
                match stat_type:
                    case "kills":
                        round_points[player] += kill_point_value * stat_value
                        total_stats[player][stat_type] += stat_value
                    case "assists":
                        round_points[player] += assist_point_value * stat_value
                        total_stats[player][stat_type] += stat_value
                    case "deaths":
                        # Si es false el jugador no murio y se le suman 5 puntos. Lo contrario se le suma 1 al contador de muertes
                        if not stat_value:
                            round_points[player] += surviving_point_value
                        else:
                            total_stats[player][stat_type] += 1 
            # Se imprime kills, assists y cantidad de muertes acumuladas ronda a ronda
            total_stats[player]['points'] += round_points[player]
        # Se calcula el mvp y se suma al total de la partida 
        for player, points in round_points.items():
            if points > points_round_mvp:
                points_round_mvp = points
                player_round_mvp = player
        total_stats[player_round_mvp]['mvp'] += 1
        print(f"{'NUEVA RONDA':*^50}")

        #Imprimimos el acumulado
        for player_name, player_stats in total_stats.items():
            print(f' El jugador {player_name}:') 
            for stat_type, stat_value in player_stats.items():  
                print(f'{stat_type:10s}: {stat_value:>3}')
        print(f'El MVP de la ronda {round_number} es {player_round_mvp} con {points_round_mvp} puntos')  
        print(f"{'FIN DE RONDA':*^50}")
