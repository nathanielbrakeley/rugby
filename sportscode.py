import xml.etree.ElementTree as ET

def parse_xml_file(fname,teams):
    tree = ET.parse(fname)
    root = tree.getroot()

    instances = {}
    for all_instances in root.iter('ALL_INSTANCES'):
        for instance in all_instances.iter('instance'):
            iid = instance.find('ID').text
            start = instance.find('start').text
            end = instance.find('end').text
            code = instance.find('code').text

            labels = []
            game_clock = None
            team = None
            player = None
            for label in instance.iter('label'):
                group = label.find('group').text
                text = label.find('text').text
                if group == 'Game Clock':
                    game_clock = text
                elif group in teams:
                    team = group
                    player = text
                else:
                    labels.append((group,text))

            instance = {
                'start': float(start),
                'end': float(end),
                'game_clock': game_clock,
                'team': team,
                'player': player,
                'labels': labels
            }
            instances[iid] = instance
    
    events = [v for k,v in instances.items()]
    events = sorted(events,key=lambda e: e['start'])

    return events