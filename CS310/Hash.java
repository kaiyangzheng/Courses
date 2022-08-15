import java.util.Iterator;
import java.util.LinkedList;

public class Hash<K,V>{
    private class HashElement<K,V> implements Comparable<HashElement<K,V>>{
        K key;
        V value;
        public HashElement(K key, V value){
            this.key = key;
            this.value = value;
        }

        public int compareTo(HashElement<K,V> o){
            return (((Comparable<K>) this.key).compareTo(o.key));
        }
    }

    int numElements;
    int tableSize;
    double maxLoadFactor;
    LinkedList<HashElement<K,V>>[] harray;

    public Hash(int tableSize){
        this.tableSize = tableSize;
        harray = (LinkedList<HashElement<K,V>>[]) new LinkedList[tableSize];
        for (int i = 0; i < tableSize; i++){
            harray[i] = new LinkedList<HashElement<K,V>>();
        }
        maxLoadFactor = 0.75;
        numElements = 0;
    }

    public double loadFactor(){
        return numElements/tableSize;
    }

    public boolean add(K key, V value){
        // if (loadFactor() > maxLoadFactor){
        //     resize(tableSize*2);
        // }

        HashElement<K,V> he = new HashElement<K,V>(key, value);
        int hashVal = key.hashCode();
        hashVal = hashVal & 0x7FFFFFFF;
        hashVal = hashVal % tableSize;
        harray[hashVal].addFirst(he);
        numElements++;
        return true;
    }

    public boolean remove(K key, V value){
        HashElement<K,V> he = new HashElement<K,V>(key, value);
        int hashVal = key.hashCode();
        hashVal = hashVal & 0x7FFFFFF;
        hashVal = hashVal % tableSize;
        harray[hashVal].remove(he);
        numElements--;
        return true;
    }
    
    public V getValue(K key){
        int hashVal = key.hashCode();
        hashVal = hashVal & 0x7FFFFFFF;
        hashVal = hashVal % tableSize;
        for (HashElement<K,V> he : harray[hashVal]){
            if (((Comparable<K>) key).compareTo(he.key) == 0){
                return he.value;
            }
        }
        return null;
    }
    // public void resize(int newSize){
    //     LinkedList<HashElement<K,V>>[] newArray = (LinkedList<HashElement<K,V>>[]) new LinkedList[newSize];
    //     for (int i = 0; i < newSize; i++){
    //         newArray[i] = new LinkedList<HashElement<K,V>>();
        
    //     }
    //     for (K key : this){
    //         V val = getValue(key);
    //         HashElement<K,V> he = new HashElement<K,V>(key, val);
    //         int hashVal = (key.hashCode() & 0x7FFFFFFF) % newSize;
    //         newArray[hashVal].add(he);
    //     }
    //     harray = newArray;
    //     tableSize = newSize;
    // }

    // class IteratorHelper<T> implements Iterator<T>{
    //     T[] keys;
    //     int position;
    //     public IteratorHelper(){
    //         keys = (T[]) new Object[numElements];
    //         int p = 0;
    //         for (int i = 0; i < tableSize; i++){
    //             LinkedList<HashElement<K,V>> list = harray[i];
    //             for (HashElement<K,V> h : list){
    //                 keys[p++] = (T) h.key;
    //             }
    //         }
    //         position = 0;
    //     }
    
    //     public boolean hasNext(){
    //         return position < keys.length;
    //     }
    
    //     public T next(){
    //         if (!hasNext()){
    //             return null;
    //         }
    //         return keys[position++];
    //     }
    // }
}