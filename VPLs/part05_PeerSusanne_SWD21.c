#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define SUCCESS 0
#define ERROR 1

// Requirement for Part 5a Memory Management in C
//
//
// a) Comments required: Add your Name
//    remove this comments or other unused lines of code
//
// b) Secure coding
//    read a (random) positive number x from the std input  
//    prepare a struct for players (name, highscore)
//    allocate memory for x players. 
//    fill each player with a generated name and start-highscore
//    e.g. input = 3
//    => player with name "Player_3" and score 3  
//    => player with name "Player_2" and score 2  
//    => player with name "Player_1" and score 1  
//    iterate over the list of players and output overall sum of highscores
//      => e.g. output Sum of highscores: '6' 
// Notice:
//    + use methods which provide error-return values
//    + check user input, check function arguments (input)
//    + allocate and initialise memory
//    + cleanup memory and set pointers to null
//    + provide error handling and cleanup when managing memory
//    beware of: 
//       type conversion, overflows, use after free, uninitialised vars
//       unterminated c-string, pointer arithmetics
// Return 
//     Warning, nothing to do.\n    <= in case of input is zero 
//     Error, input out of scope.\n <= in case of input > 999 (or negative)
//     Sum of highscores '6'\n      <= in case of input is ok 

// NOTE: ONLY ONE OUTPUT is allowed
//       remove / comment all other print statements in your code




// max 999_999
int get_the_input(int* num){
  // check if pointer is ok
  if (NULL == num){
    return ERROR;
  }
  
  char buf[7]; // we allow max of 6 chars and return \n
  char* res = fgets(buf, sizeof buf, stdin);
  
  // did we get input?
  if (NULL == res){
    // printf("ERROR: VPL and C — Input too long given buffer. Max 6 chars allowed.");
    return ERROR;
  }
  
  // remove trailling return if available
  if (buf[strlen(buf)-1] == '\n') {
    buf[strlen(buf)-1] = 0;
  }

  // len = strlen(buf); // len including terminating \0
  // printf("We read in %d chars: '%s'.\n",len,buf);  

  *num = atoi(res);  
  return SUCCESS;
}




/*  
BEGIN - ADD YOIÚR CODE HERE 
*/

// add some more functions if needed
  

typedef struct {
	char* name;
  // ...
  // ...
  //  ...
	
} Player;

int sum_it(int no_of_players, int* sum){
	int result = ERROR;
	//printf("A) Prepare data structure for %d players:\n",no_of_players);
	Player* players[no_of_players];
	//printf(" For each player\n");
	for (int i=0;i<no_of_players;i++){
		//printf("  %d/%d alloc memory\n",i+1,no_of_players);
		Player* p;
		//  ...
		char* name;
		name = calloc(1,10);
		//  ...
		sprintf(name, "Player_%d",i+1); 
		p->name = name;
		players[i] = p;
		//printf("  %d/%d player '%s' is ready.\n",i+1,no_of_players,p->name);
	}
	
	//printf("B) For each of the %d players read score and add to sum:\n",no_of_players);
	for (int i=0;i<no_of_players;i++){
		Player* p = players[i];
		//  ...
		//printf(" %d/%d player added %d to current sum of %d.\n",i+1,no_of_players, p->score,*sum);
	}
	
	result = SUCCESS;
 cleanup:
	//printf("C) Free memory for all the %d players:\n",no_of_players);
	for (int i=0;i<no_of_players;i++){
        Player* p;
        //  ...
		//printf("  %d/%d player free memory.\n",i+1,no_of_players);
		free(p);
		p=NULL;
	}
	//printf("Done function sum-it with return code:  %d. Sum = %d.\n\n",result,*sum);
	return result;
}

  

/*  
END — ADD YOIÚR CODE HERE 
*/



int main(){
  int inp =0;
  int res = SUCCESS;

  // we expect some input from std-in
  // e.g. piped into this program with echo "123" | ./a.out
  res = get_the_input(&inp);
  if (SUCCESS != res){
    printf("Error, input out of scope.\n"); 
    return res;
  }
  
  int result = 0;
  
  /*  
  BEGIN - ADD YOUR CODE HERE 
  */

  // ...
  // ...
  //  ...

    int sum = 0;
	res = sum_it(inp, &sum);
	if (SUCCESS == res){
	    printf("Sum of highscores: '%d'\n",sum);    		
	}else{
	    printf("Error %d calculating the sum of scores.'\n",res);    
	}

 //  ...
  
  
  /*  
  END — ADD YOÚR CODE HERE 
  */
  
  return res;
}
