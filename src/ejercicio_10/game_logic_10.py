from .functions_10 import *

def run_game(rounds):
    # Se define el criterio del puntaje
    kill_point_value = 3
    assist_point_value = 1
    death_point_value = 1

    # Se inicializa las variables necesarias para acumular el puntaje
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
    # Se recorre la lista, se accede al diccionario de cada ronda.
    for round in rounds:
        round_number += 1
        # Se resetean e inicializa los puntajes de la ronda
        round_points = round_points_initial.copy()
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
                        if stat_value:
                            round_points[player] -= death_point_value
                            total_stats[player][stat_type] += 1          
            # Se imprime kills, assists y cantidad de muertes acumuladas ronda a ronda
            total_stats[player]['points'] += round_points[player]
        # Se calcula el mvp y se suma al total de la partida 
        round_mvp = calculate_mvp(round_points)
        round_mvp_name = list(round_mvp.keys())[0] # Una forma mas compacta next(iter(round_mvp))
        total_stats[round_mvp_name]['mvp'] += 1
        #Imprimimos el acumulado y el mvp por ronda
        print_rounds(total_stats, round_number, round_mvp_name, round_mvp[round_mvp_name])
    #Se retorna el jugador o jugadores que fueron mas veces el mvp durante las rondas. 
    max_value = max(total_stats.values(), key=lambda x: x['mvp'])['mvp']
    max_mvps = [player for player, stats in total_stats.items() if stats['mvp'] == max_value]
    if len(max_mvps) == 1:
        print(f"{'-':-^50}")
        print(f'\n El MVP de la partida es {max_mvps[0]} siendo {max_value} veces MVP\n')
        print(f"{'-':-^50}")
    else:
        print(f"{'-':-^50}")
        print(f'\n Los MVP de la partida son {max_mvps} siendo {max_value} veces MVP\n')
        print(f"{'-':-^50}")