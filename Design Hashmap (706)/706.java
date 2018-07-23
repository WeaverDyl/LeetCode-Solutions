// Runtime: 244 ms (???)
// Beats 1.63% of Java submissions (Essentially equal implementations ran in ~110 ms, something's up)

class MyHashMap {
    Integer[] hashMap;
    /** Initialize your data structure here. */
    public MyHashMap() {
        this.hashMap = new Integer[10000001];
    }
    
    /** value will always be non-negative. */
    public void put(int key, int value) {
        hashMap[key] = value;
    }
    
    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    public int get(int key) {
        if (hashMap[key] == null) {
            return -1;
        }
        return hashMap[key];
    }
    
    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    public void remove(int key) {
        hashMap[key] = -1;
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */