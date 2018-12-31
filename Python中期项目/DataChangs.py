#! /usr/bin/env python
import Attribute
def buy(player,map):
    '''定义土地购买事件'''
    player.cash -= map.price
    player.land += 1
    player.money = player.cash + player.deposit
    map.belong = player.name
buy(player1,map)
player1.show()
print(map.belong)



