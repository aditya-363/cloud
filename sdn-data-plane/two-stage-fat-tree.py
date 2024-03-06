#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.util import dumpNodeConnections
from mininet.link import Link, Intf, TCLink
import os 
from time import sleep
import sys

# N = switch size (number of ports in a switch)
N = 4

class Topology(Topo):

    def __init__(self):
        "Create Topology."
        
        # Initialize topology
        Topo.__init__(self)
        
        #### There is a rule of naming the hosts and switch, so please follow the rules like "h1", "h2" or "s1", "s2" for hosts and switches!!!!

        HALF_N = N // 2
        hostCount = N * HALF_N
        edgeSwitchCount = N
        coreSwitchCount = HALF_N
        
        
        hosts = [self.addHost("h{}".format(i)) for i in range(1, hostCount + 1)]
        edgeSwitches = [self.addSwitch("s{}".format(i) ) for i in range(1, edgeSwitchCount + 1)]
        coreSwitches = [self.addSwitch("s{}".format(i) ) for i in range(edgeSwitchCount + 1, edgeSwitchCount + coreSwitchCount + 1)]

        for i, host in enumerate(hosts):
            self.addLink(edgeSwitches[i % edgeSwitchCount], host)
        for edge in edgeSwitches:
            for core in coreSwitches:
                self.addLink(edge, core)


# This is for "mn --custom"
topos = { 'mytopo': ( lambda: Topology() ) }


# This is for "python *.py"
if __name__ == '__main__':
    setLogLevel( 'info' )
            
    topo = Topology()
    net = Mininet(topo=topo, link=TCLink)       # The TCLink is a special setting for setting the bandwidth in the future.
    
    # 1. Start mininet
    net.start()

    # Wait for links setup (sometimes, it takes some time to setup, so wait for a while before mininet starts)
    print "\nWaiting for links to setup . . . .",
    sys.stdout.flush()
    for time_idx in range(3):
        print ".",
        sys.stdout.flush()
        sleep(1)
        
    # 2. Start the CLI commands
    info( '\n*** Running CLI\n' )
    CLI( net )
    
    # 3. Stop mininet properly
    net.stop()

    ### If you did not close the mininet, please run "mn -c" to clean up and re-run the mininet 
