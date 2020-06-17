from sportscode import parse_xml_file
import matplotlib.pyplot as plt
import json

def main():
    teams = ['Rugby United New York','Rugby ATL']
    filename = 'ATL_RUNY.xml'

    # Parse XML file
    events = parse_xml_file(filename,teams)

    fa_lookup = field_area_lookup()
    lr_lookup = left_right_lookup()

    positions = []
    for e in events:
        labels = e['labels']
        fa = next((l[1] for l in labels if l[0] == 'Field Area'),None)
        lr = next((l[1] for l in labels if l[0] == 'Field L-R'),None)

        if fa and lr:
            positions.append((fa_lookup[fa],lr_lookup[lr]))

    print(len(positions))
    plot(positions)

def field_area_lookup():
    return {
        '22 - GL': 4,
        '50 - 22': 3, 
        '22 - 50': 2, 
        'GL - 22': 1, 
    }

def left_right_lookup():
    return {
        'L': 1,
        'CL': 2, 
        'C': 3,  
        'CR': 4, 
        'R': 5
    }


def plot(positions):
    # plt.ion()
    print('here')
    x = [p[0] for p in positions]
    y = [p[1] for p in positions]

    plt.plot(x,y,'o')
    plt.show()


    # time = range(0,100)
    # momentum = [t*t for t in time]

    # for i in range(0,len(time)):
    #     plt.plot(time[0:i],momentum[0:i],'o')
    #     plt.draw()
    #     plt.pause(0.001)
    #     plt.clf()


if __name__ == '__main__':
    main()
    