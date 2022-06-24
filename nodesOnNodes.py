import requests
import json
import timeit

def sendReq(node_id):
    #print("Sending req %s" % node_id)
    r = requests.get('https://nodes-on-nodes-challenge.herokuapp.com/nodes/%s' % node_id,
            headers={'Accept': 'application/json'})
    result = r.json()
    return result

def collectChildNodes(node_id, seen):
    #print("Collecting child nodes from %s" % node_id)
    result = sendReq(node_id)
    for res in result:
        for ch_id in res.get('child_node_ids'):
            if ch_id in seen.keys():
                seen[ch_id] = seen[ch_id]+1
            else:
                seen[ch_id] = 1
                collectChildNodes(ch_id, seen)

def main():
    start = timeit.default_timer()
    print("Begin program")
    start_node_id = "089ef556-dfff-4ff2-9733-654645be56fe"
    seen = {start_node_id: 1}
    collectChildNodes(start_node_id, seen)

    print("Seen: %s" % str(seen))
    print("Total unique nodes: %s" % len(seen.keys()))
    commonNode = [key for key, value in seen.items() if value == max(seen.values())]
    print("Most common node(s) ID: %s" % commonNode)
    stop = timeit.default_timer()
    print("Finished in %s" % (stop-start))


if __name__ == '__main__':
    main()
