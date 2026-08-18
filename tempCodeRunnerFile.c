#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>


int main() {
    pid_t pid = fork();

    if (pid < 0) {
        fprintf(stderr,"fork Execution failed");
        return 1;
    }
    else if (pid == 0) {
        // Child Process segment
        printf("[CHILD] Active Process ID: %d ",getpid());
        printf("[CHILD] Parent Process ID: %d ", getppid());
    }
    else {
        //parents process segment
        wait(NULL); // sync wrapper insuring the child completes execution first
        printf("[PARENT] child finished. parent process ID: %d", getpid());
    }
    return 0 ;
}