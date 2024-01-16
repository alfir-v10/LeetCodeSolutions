[Find Players With Zero or One Losses](https://leetcode.com/problems/find-players-with-zero-or-one-losses)
```Python
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        player_stats = {}
        for winner, loser in matches:
            if winner not in player_stats:
                player_stats.update({winner: 0})
            if loser not in player_stats:
                player_stats.update({loser: 1})
            elif loser in player_stats:
                player_stats[loser] += 1
        no_one = []
        only_one = []
        for player, stat in player_stats.items():
            if stat == 0:
                no_one.append(player)
            if stat == 1:
                only_one.append(player)
        no_one.sort()
        only_one.sort()
        return list([no_one, only_one])
```