int min(int a, int b) {
    return a < b ? a : b;
}
int maxArea(int* height, int heightSize) {
    int esq = 0;
    int dir = heightSize -1;
    int maxAtual = min(height[esq], height[dir]) * 1;
    
    while(esq < dir){
        int dist = dir - esq;
        int menor = min(height[esq], height[dir]);
        if(menor * dist > maxAtual){
            maxAtual = menor * dist;
        }
        if(height[esq] < height[dir]){
            esq++;
        } else {
            dir--;
        }
    }
    return maxAtual;
    
}