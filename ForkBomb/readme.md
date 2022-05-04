# Fork Bomb

The fork bomb attack uses a specific syntax to create two new processes for every one process and continues to call itself with recursion. It is an infinite
loop that continues to create processes until the system. It slowly takes over system resources until the system crashes or needs to be restarted. The results
section shows the what happens when the script is run twice. The first screenshot shows how it states it is unable to fork and conitnues to try to do so.
The second screenshot shows that I was able to ping and use the machine after the attack demonstrating that the machine did not go down during the attack. 
This is because the system is properly configured to limit the amount of processes a user can run.
