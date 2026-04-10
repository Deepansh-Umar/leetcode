class RecentCounter {
    Queue<Integer> q;
    int c;
    public RecentCounter() {
        this.c=0;
        this.q = new LinkedList<>();
    }
    
    public int ping(int t) {
        this.q.offer(t);
        while(!this.q.isEmpty()){
            int v = this.q.peek();
            if (v>= t-3000){
                break;
            }else{
                this.q.poll();
            }
        }
        return this.q.size();
    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter obj = new RecentCounter();
 * int param_1 = obj.ping(t);
 */