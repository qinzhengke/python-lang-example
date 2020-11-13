// Export with C-style, "extern C" is necessary.
#include <math.h>

struct Point{
    double x,y;
};

extern "C"{

double add(double x, double y){
    return x + y;
}

double average(double *num, int N){
    if(0 == N){
        return 0;
    }

    double sum = 0.0;
    for(int i=0; i<N; i++){
        sum += num[i];
    }
    return sum / N;
}

double distance(struct Point *p1, struct Point *p2){
    return sqrt((p1->x-p2->x)*(p1->x-p2->x)+(p1->y-p2->y)*(p1->y-p2->y));
}

}