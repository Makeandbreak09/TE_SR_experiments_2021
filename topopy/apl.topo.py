
#!/usr/bin/env python3
from node import *

class apl(Topo):
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
        self.add_link_name("0", "3", cost=1000, delay=0.2, bw=100000000000000, directed=True)
        self.add_link_name("3", "0", cost=1000, delay=0.2, bw=100000000000000, directed=True)
        self.add_link_name("0", "1", cost=1000, delay=0.2, bw=100000000000000, directed=True)
        self.add_link_name("1", "0", cost=1000, delay=0.2, bw=100000000000000, directed=True)
        self.add_link_name("0", "4", cost=1000, delay=0.2, bw=10000000000000, directed=True)
        self.add_link_name("4", "0", cost=1000, delay=0.2, bw=10000000000000, directed=True)
        self.add_link_name("1", "2", cost=1000, delay=0.2, bw=80000000000000, directed=True)
        self.add_link_name("2", "1", cost=1000, delay=0.2, bw=80000000000000, directed=True)
        self.add_link_name("1", "4", cost=1000, delay=0.2, bw=100000000000000, directed=True)
        self.add_link_name("4", "1", cost=1000, delay=0.2, bw=100000000000000, directed=True)
        self.add_link_name("1", "5", cost=1000, delay=0.2, bw=100000000000000, directed=True)
        self.add_link_name("5", "1", cost=1000, delay=0.2, bw=100000000000000, directed=True)
        self.add_link_name("2", "5", cost=1000, delay=0.2, bw=80000000000000, directed=True)
        self.add_link_name("5", "2", cost=1000, delay=0.2, bw=80000000000000, directed=True)
        self.add_link_name("3", "6", cost=1000, delay=0.2, bw=100000000000000, directed=True)
        self.add_link_name("6", "3", cost=1000, delay=0.2, bw=100000000000000, directed=True)
        self.add_link_name("3", "4", cost=1000, delay=0.2, bw=100000000000000, directed=True)
        self.add_link_name("4", "3", cost=1000, delay=0.2, bw=100000000000000, directed=True)
        self.add_link_name("3", "7", cost=1000, delay=0.2, bw=100000000000000, directed=True)
        self.add_link_name("7", "3", cost=1000, delay=0.2, bw=100000000000000, directed=True)
        self.add_link_name("4", "5", cost=1000, delay=0.2, bw=15000000000000, directed=True)
        self.add_link_name("5", "4", cost=1000, delay=0.2, bw=15000000000000, directed=True)
        self.add_link_name("4", "8", cost=1000, delay=0.2, bw=10000000000000, directed=True)
        self.add_link_name("8", "4", cost=1000, delay=0.2, bw=10000000000000, directed=True)
        self.add_link_name("4", "7", cost=1000, delay=0.2, bw=100000000000000, directed=True)
        self.add_link_name("7", "4", cost=1000, delay=0.2, bw=100000000000000, directed=True)
        self.add_link_name("5", "8", cost=1000, delay=0.2, bw=80000000000000, directed=True)
        self.add_link_name("8", "5", cost=1000, delay=0.2, bw=80000000000000, directed=True)
        self.add_link_name("6", "7", cost=1000, delay=0.2, bw=100000000000000, directed=True)
        self.add_link_name("7", "6", cost=1000, delay=0.2, bw=100000000000000, directed=True)
        self.add_link_name("7", "8", cost=1000, delay=0.2, bw=100000000000000, directed=True)
        self.add_link_name("8", "7", cost=1000, delay=0.2, bw=100000000000000, directed=True)
    
    def dijkstra_computed(self):
        # Demand from 0 to 5
        build_str = ""
        nhlist = self.get_dijkstra_route_by_name("0","1")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+" encap seg6 mode inline segs {1} "+ f" weight {int(100/len(nhlist))} "
        self.add_command("0", f"ip -6 route add {{5}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 0 to 7
        build_str = ""
        nhlist = self.get_dijkstra_route_by_name("0","3")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+" encap seg6 mode inline segs {3} "+ f" weight {int(100/len(nhlist))} "
        self.add_command("0", f"ip -6 route add {{7}} metric 1 table 1 src {{0}}  {build_str}")
        # Demand from 4 to 8
        build_str = ""
        nhlist = self.get_dijkstra_route_by_name("4","7")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+" encap seg6 mode inline segs {7} "+ f" weight {int(100/len(nhlist))} "
        self.add_command("4", f"ip -6 route add {{8}} metric 1 table 1 src {{4}}  {build_str}")
        # Demand from 1 to 8
        build_str = ""
        nhlist = self.get_dijkstra_route_by_name("1","7")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+" encap seg6 mode inline segs {7} "+ f" weight {int(100/len(nhlist))} "
        self.add_command("1", f"ip -6 route add {{8}} metric 1 table 1 src {{1}}  {build_str}")
        # Demand from 8 to 0
        build_str = ""
        nhlist = self.get_dijkstra_route_by_name("8","7")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+" encap seg6 mode inline segs {7} "+ f" weight {int(100/len(nhlist))} "
        self.add_command("8", f"ip -6 route add {{0}} metric 1 table 1 src {{8}}  {build_str}")
        self.add_command("0", "ip -6 rule add to {5/} iif lo table 1")
        self.add_command("0", "ip -6 rule add to {7/} iif lo table 1")
        self.add_command("4", "ip -6 rule add to {8/} iif lo table 1")
        self.add_command("1", "ip -6 rule add to {8/} iif lo table 1")
        self.add_command("8", "ip -6 rule add to {0/} iif lo table 1")
        self.add_command("8", "nuttcp -6 -S")
        self.add_command("0", "nuttcp -6 -S")
        self.add_command("5", "nuttcp -6 -S")
        self.add_command("7", "nuttcp -6 -S")
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R100000 -N32 {5} \>\>flow_0-5.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-5.txt\; done\\\" | at now+2min')
        self.add_command("0", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 0 nuttcp -T300 -i1 -R100000 -N32 {7} \>\>flow_0-7.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_0-7.txt\; done\\\" | at now+2min')
        self.add_command("4", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 4 nuttcp -T300 -i1 -R100000 -N32 {8} \>\>flow_4-8.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_4-8.txt\; done\\\" | at now+2min')
        self.add_command("1", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 1 nuttcp -T300 -i1 -R100000 -N32 {8} \>\>flow_1-8.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_1-8.txt\; done\\\" | at now+2min')
        self.add_command("8", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 8 nuttcp -T300 -i1 -R100000 -N32 {0} \>\>flow_8-0.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_8-0.txt\; done\\\" | at now+2min')

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

topos = {'apl': (lambda: apl())}

