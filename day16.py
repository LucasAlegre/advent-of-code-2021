from dataclasses import dataclass
from math import prod
from typing import List

def read_input(filename='inputs/day16.txt'):
    with open(filename) as f:
        packet = f.read().strip()
    return ''.join(bin(int(x, 16))[2:].zfill(4) for x in packet)

@dataclass
class Packet:
    version: int
    typeid: int
    number: int
    size: int
    subpackets: List['Packet']

    def __post_init__(self):
        if self.typeid == 0:
            self.number = sum(p.number for p in self.subpackets)
        elif self.typeid == 1:
            self.number = prod(p.number for p in self.subpackets)
        elif self.typeid == 2:
            self.number = min(p.number for p in self.subpackets)
        elif self.typeid == 3:
            self.number = max(p.number for p in self.subpackets)
        elif self.typeid == 5:
            self.number = 1 if self.subpackets[0].number > self.subpackets[1].number else 0
        elif self.typeid == 6:
            self.number = 1 if self.subpackets[0].number < self.subpackets[1].number else 0
        elif self.typeid == 7:
            self.number = 1 if self.subpackets[0].number == self.subpackets[1].number else 0

def parse(packet):
    version = int(packet[:3], 2)
    typeid = int(packet[3:6], 2)
    data = packet[6:]
    size = 6
    subpackets = []
    if typeid == 4:
        number = ''
        finished = False
        while not finished:
            size += 5
            number += data[1:5]
            if data[0] == '0':
                finished = True
            data = data[5:]
        number = int(number, 2)
        return Packet(version, typeid, number, size, []), data
    else:
        lenghtypeid = data[0]
        size += 1
        if lenghtypeid == '0':
            length_subpacket = int(data[1:16], 2)
            subpackets_data = data[16:16 + length_subpacket]
            size += 15 + length_subpacket
            while subpackets_data != '':
                packet, subpackets_data = parse(subpackets_data)
                subpackets.append(packet)
            return Packet(version, typeid, None, size, subpackets), data[16 + length_subpacket:]
        else:
            num_subpackets = int(data[1:12], 2)
            size += 11
            subpackets_data = data[12:]
            for _ in range(num_subpackets):
                packet, subpackets_data = parse(subpackets_data)
                size += packet.size
                subpackets.append(packet)
            return Packet(version, typeid, None, size, subpackets), data[size - 6:]

def total_version(packet):
    total = packet.version
    for p in packet.subpackets:
        total += total_version(p)
    return total

def part1(packet):
    packet, _ = parse(packet)
    return total_version(packet)

def part2(packet):
    packet, _ = parse(packet)
    return packet.number

packet = read_input()
print(part1(packet))
print(part2(packet))