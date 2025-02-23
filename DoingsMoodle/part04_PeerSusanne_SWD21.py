package main

// Requirement for Part 4b Concurrency with Go
//
// Susanne Peer SWD21
//
// b) Multithreading:
//    Simulate concurrent "downloading of x files with the size of 7 MB each"
//    return the final amount of MB downloaded.
//    REQUIRED: a go function for each download,
//             (concurrent) waiting 2 secs for each download
//              use of channels for synchronisation
// NOTE: ONLY ONE OUTPUT is allowed
//       keep line 34: fmt.Printf("RESULT: '%v'", res)
//       remove / comment all other print statements in your code

import (
	"bufio" // input = we read (buffered) text from stdin
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

func main() {
	res := ""
	scanner := bufio.NewReader(os.Stdin)         // read from STDIN
	input, _ := scanner.ReadString('\n')         // read FIRST line
	input = strings.Replace(input, "\n", "", -1) // remove line break

	res = myalgo(input) // caluclate the result

	fmt.Printf("RESULT: '%v'", res) // return the result
}

func myalgo(input string) string { // input string
	val, _ := strconv.Atoi(input)
	//fmt.Printf("Just if you need it... the value converted to integer: %d\n", val)

	c := make(chan int)
	
	go download(c)
	go download(c)
	go download(c)

	totalDownloaded := 0
	for i := 0; i < 3; i++{
		downloaded := <-c
		totalDownloaded += downloaded
	}

	return strconv.Itoa(val) // return string
}

func download(c chan int) {
	time.Sleep(2*time.Second)
	c <- 7
}

