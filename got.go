package main

import (
	"fmt"
	"net"
	"runtime"
	"strings"
)

func isUp(nif *net.Interface) bool       { return nif.Flags&net.FlagUp != 0 }
func isLoopback(nif *net.Interface) bool { return nif.Flags&net.FlagLoopback != 0 }

func isProblematicInterface(nif *net.Interface) bool {
	name := nif.Name
	// Don't try to send disco/etc packets over zerotier; they effectively
	// DoS each other by doing traffic amplification, both of them
	// preferring/trying to use each other for transport. See:
	// https://github.com/tailscale/tailscale/issues/1208
	if strings.HasPrefix(name, "zt") || (runtime.GOOS == "windows" && strings.Contains(name, "ZeroTier")) {
		return true
	}
	return false
}

func main() {
	interfaces, err := net.Interfaces()
	if err != nil {
		panic(err)
	}

	for _, iface := range interfaces {
		if isProblematicInterface(&iface) {
			fmt.Printf("Interface %s is considered problematic.\n", iface.Name)
		} else {
			fmt.Printf("Interface %s is NOT considered problematic.\n", iface.Name)
		}
	}
}