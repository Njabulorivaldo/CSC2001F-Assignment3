class HashTableFunctions
{
   // hash function weights.
   // 9 integers, each in the range 0-5 to act as weights for the characters in the keys.
    public int [] weights = {1, 4, 2, 4, 3, 2, 1, 4, 3};;
   
   
   public HashTableFunctions(int[] weights){
   	this.weights = weights;
   }
   // ADD YOUR WEIGHTS INSTEAD OF 1s

   // returns True if the hash table contains string s
   // return False if the hash table does not contain string s
   boolean find ( String s, int pos, int hashTableSize, String [] hashTableArray )
   {
      // WRITE YOUR CODE HERE
      
      while (!hashTableArray[pos].equals("")) {
      
      		if(hashTableArray[pos].equals(s))
      			return true;
      		else {
      			pos++;
      			pos = pos%hashTableSize;
      			}
      }
      return false;
   }
}
