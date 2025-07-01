
#!/usr/bin/env python3
from node import *

class LLLF(Topo):
    def build(self):
        self.add_node("0")
        self.add_node("1")
        self.add_node("2")
        self.add_node("3")
        self.add_node("4")
        self.add_node("5")
        self.add_node("6")
        self.add_node("7")
        self.add_node("8")
        self.add_node("9")
        self.add_node("10")
        self.add_link_name("6", "7", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("7", "6", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("0", "2", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("2", "0", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("0", "6", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("6", "0", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("0", "8", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("8", "0", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("1", "2", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("2", "1", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("1", "3", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("3", "1", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("1", "4", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("4", "1", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("1", "5", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("5", "1", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("1", "7", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("7", "1", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("3", "7", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("7", "3", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("3", "8", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("8", "3", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("5", "7", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("7", "5", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("2", "5", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("5", "2", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("2", "7", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("7", "2", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("2", "8", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("8", "2", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("4", "5", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("5", "4", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("4", "7", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("7", "4", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("4", "8", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("8", "4", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("9", "8", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("8", "9", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("7", "9", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("9", "7", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("3", "9", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("9", "3", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("0", "10", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("10", "0", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("1", "10", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("10", "1", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("10", "6", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("6", "10", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("10", "7", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("7", "10", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("10", "3", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("3", "10", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("6", "3", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("3", "6", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("6", "9", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("9", "6", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("0", "9", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("9", "0", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("1", "9", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("9", "1", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("2", "9", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("9", "2", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("0", "1", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("1", "0", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("10", "2", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("2", "10", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("2", "4", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("4", "2", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("5", "9", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("9", "5", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("6", "8", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("8", "6", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("0", "7", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("7", "0", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("10", "5", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("5", "10", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("10", "8", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("8", "10", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("3", "4", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("4", "3", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("4", "6", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("6", "4", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("3", "5", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
        self.add_link_name("5", "3", cost=1000, delay=0.2, bw=1000000000000.0, directed=True)
    
    def dijkstra_computed(self):
        # Demand from 8 to 1
        build_str = ""
        nhlist = self.get_dijkstra_route_by_name("8","0")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+" encap seg6 mode inline segs {0} "+ f" weight {int(100/len(nhlist))} "
        nhlist = self.get_dijkstra_route_by_name("8","1")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+ f" weight {int(100/len(nhlist))} "
        self.add_command("8", f"ip -6 route add {{1}} metric 1 table 1 src {{8}}  {build_str}")
        # Demand from 8 to 1
        build_str = ""
        nhlist = self.get_dijkstra_route_by_name("8","2")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+" encap seg6 mode inline segs {2} "+ f" weight {int(100/len(nhlist))} "
        nhlist = self.get_dijkstra_route_by_name("8","1")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+ f" weight {int(100/len(nhlist))} "
        self.add_command("8", f"ip -6 route add {{1}} metric 1 table 1 src {{8}}  {build_str}")
        # Demand from 8 to 1
        build_str = ""
        nhlist = self.get_dijkstra_route_by_name("8","3")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+" encap seg6 mode inline segs {3} "+ f" weight {int(100/len(nhlist))} "
        nhlist = self.get_dijkstra_route_by_name("8","1")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+ f" weight {int(100/len(nhlist))} "
        self.add_command("8", f"ip -6 route add {{1}} metric 1 table 1 src {{8}}  {build_str}")
        # Demand from 8 to 1
        build_str = ""
        nhlist = self.get_dijkstra_route_by_name("8","4")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+" encap seg6 mode inline segs {4} "+ f" weight {int(100/len(nhlist))} "
        nhlist = self.get_dijkstra_route_by_name("8","1")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+ f" weight {int(100/len(nhlist))} "
        self.add_command("8", f"ip -6 route add {{1}} metric 1 table 1 src {{8}}  {build_str}")
        # Demand from 8 to 1
        build_str = ""
        nhlist = self.get_dijkstra_route_by_name("8","9")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+" encap seg6 mode inline segs {9} "+ f" weight {int(100/len(nhlist))} "
        nhlist = self.get_dijkstra_route_by_name("8","1")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+ f" weight {int(100/len(nhlist))} "
        self.add_command("8", f"ip -6 route add {{1}} metric 1 table 1 src {{8}}  {build_str}")
        # Demand from 6 to 4
        build_str = ""
        nhlist = self.get_dijkstra_route_by_name("6","4")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+ f" weight {int(100/len(nhlist))} "
        self.add_command("6", f"ip -6 route add {{4}} metric 1 table 1 src {{6}}  {build_str}")
        # Demand from 6 to 4
        build_str = ""
        nhlist = self.get_dijkstra_route_by_name("6","3")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+" encap seg6 mode inline segs {3} "+ f" weight {int(100/len(nhlist))} "
        nhlist = self.get_dijkstra_route_by_name("6","4")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+ f" weight {int(100/len(nhlist))} "
        self.add_command("6", f"ip -6 route add {{4}} metric 1 table 1 src {{6}}  {build_str}")
        # Demand from 6 to 4
        build_str = ""
        nhlist = self.get_dijkstra_route_by_name("6","7")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+" encap seg6 mode inline segs {7} "+ f" weight {int(100/len(nhlist))} "
        nhlist = self.get_dijkstra_route_by_name("6","4")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+ f" weight {int(100/len(nhlist))} "
        self.add_command("6", f"ip -6 route add {{4}} metric 1 table 1 src {{6}}  {build_str}")
        # Demand from 6 to 4
        build_str = ""
        nhlist = self.get_dijkstra_route_by_name("6","10")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+" encap seg6 mode inline segs {10} "+ f" weight {int(100/len(nhlist))} "
        nhlist = self.get_dijkstra_route_by_name("6","1")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+" encap seg6 mode inline segs {1} "+ f" weight {int(100/len(nhlist))} "
        nhlist = self.get_dijkstra_route_by_name("6","4")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+ f" weight {int(100/len(nhlist))} "
        self.add_command("6", f"ip -6 route add {{4}} metric 1 table 1 src {{6}}  {build_str}")
        # Demand from 6 to 4
        build_str = ""
        nhlist = self.get_dijkstra_route_by_name("6","0")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+" encap seg6 mode inline segs {0} "+ f" weight {int(100/len(nhlist))} "
        nhlist = self.get_dijkstra_route_by_name("6","2")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+" encap seg6 mode inline segs {2} "+ f" weight {int(100/len(nhlist))} "
        nhlist = self.get_dijkstra_route_by_name("6","4")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+ f" weight {int(100/len(nhlist))} "
        self.add_command("6", f"ip -6 route add {{4}} metric 1 table 1 src {{6}}  {build_str}")
        self.add_command("8", "ip -6 rule add to {1/} iif lo table 1")
        self.add_command("8", "ip -6 rule add to {1/} iif lo table 1")
        self.add_command("8", "ip -6 rule add to {1/} iif lo table 1")
        self.add_command("8", "ip -6 rule add to {1/} iif lo table 1")
        self.add_command("8", "ip -6 rule add to {1/} iif lo table 1")
        self.add_command("6", "ip -6 rule add to {4/} iif lo table 1")
        self.add_command("6", "ip -6 rule add to {4/} iif lo table 1")
        self.add_command("6", "ip -6 rule add to {4/} iif lo table 1")
        self.add_command("6", "ip -6 rule add to {4/} iif lo table 1")
        self.add_command("6", "ip -6 rule add to {4/} iif lo table 1")
        self.add_command("1", "nuttcp -6 -S")
        self.add_command("4", "nuttcp -6 -S")
        self.add_command("8", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 8 nuttcp -T300 -i1 -R12000 -N32 {1} \>\>flow_8-1.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_8-1.txt\; done\\\" | at now+2min')
        self.add_command("8", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 8 nuttcp -T300 -i1 -R12000 -N32 {1} \>\>flow_8-1.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_8-1.txt\; done\\\" | at now+2min')
        self.add_command("8", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 8 nuttcp -T300 -i1 -R12000 -N32 {1} \>\>flow_8-1.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_8-1.txt\; done\\\" | at now+2min')
        self.add_command("8", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 8 nuttcp -T300 -i1 -R12000 -N32 {1} \>\>flow_8-1.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_8-1.txt\; done\\\" | at now+2min')
        self.add_command("8", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 8 nuttcp -T300 -i1 -R12000 -N32 {1} \>\>flow_8-1.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_8-1.txt\; done\\\" | at now+2min')
        self.add_command("6", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 6 nuttcp -T300 -i1 -R12000 -N32 {4} \>\>flow_6-4.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_6-4.txt\; done\\\" | at now+2min')
        self.add_command("6", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 6 nuttcp -T300 -i1 -R12000 -N32 {4} \>\>flow_6-4.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_6-4.txt\; done\\\" | at now+2min')
        self.add_command("6", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 6 nuttcp -T300 -i1 -R12000 -N32 {4} \>\>flow_6-4.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_6-4.txt\; done\\\" | at now+2min')
        self.add_command("6", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 6 nuttcp -T300 -i1 -R12000 -N32 {4} \>\>flow_6-4.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_6-4.txt\; done\\\" | at now+2min')
        self.add_command("6", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 6 nuttcp -T300 -i1 -R12000 -N32 {4} \>\>flow_6-4.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_6-4.txt\; done\\\" | at now+2min')

        self.enable_throughput()
        self.add_command("0", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("1", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("2", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("3", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("4", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("5", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("6", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("7", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("8", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("9", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("10", "sysctl net.ipv6.fib_multipath_hash_policy=1")

topos = {'LLLF': (lambda: LLLF())}
