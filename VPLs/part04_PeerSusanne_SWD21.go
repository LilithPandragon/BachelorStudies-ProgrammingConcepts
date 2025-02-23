package main

// Part 4b Concurrency with Go
//  Susanne Peer, SWD 21



import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

func main() {
	res := ""
	scanner := bufio.NewReader(os.Stdin)
	input, _ := scanner.ReadString('\n')
	input = strings.Replace(input, "\n", "", -1)

	res = myalgo(input)
	fmt.Printf("RESULT: '%v'", res)
}

func myalgo(input string) string {
	val, _ := strconv.Atoi(input)

	resultChannel := make(chan int)


	for i := 0; i < val; i++ {
		go download(resultChannel)
	}


	totalDownloaded := 0
	for i := 0; i < val; i++ {
		downloadedSize := <-resultChannel
		totalDownloaded += downloadedSize
	}

	return strconv.Itoa(totalDownloaded)
}

func download(c chan int) {

	time.Sleep(2 * time.Second)

	// Simulate downloading a 7 MB file
	c <- 7
}
