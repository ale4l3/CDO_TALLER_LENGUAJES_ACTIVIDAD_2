def print_rounds(total_stats, round_number, round_mvp_name, round_mvp_points): 
    print(f"\n{' NUEVA RONDA ' + str(round_number) + ' ':*^50}")
    for player_name, player_stats in total_stats.items():
        print(f' El jugador {player_name}:') 
        for stat_type, stat_value in player_stats.items():  
            print(f'{stat_type:10s}: {stat_value:>3}')
    print(f"{'-':-^50}")
    print(f'\n MVP en la ronda {round_number} es {round_mvp_name} con {round_mvp_points} puntos \n')
    print(f"{'-':-^50}")
    print(f"{'FIN DE RONDA':*^50}")

def calculate_mvp(round_points):
        points_round_mvp = 0
        player_round_mvp = 'zzz'
        for player, points in round_points.items():
            if points > points_round_mvp:
                points_round_mvp = points
                player_round_mvp = player
        return {player_round_mvp: points_round_mvp}