#include <iostream>
using namespace std;
#define max 20

class stud{
    public:
    int mks[max];
    stud(){
        for(int i=0; i<max ; i++){
            mks[i] = 0;
        }
    }
    
    void insertData(int total);
    void minMarks();
    void maxMarks(int total);
    void displayHeap(int total);
};

void stud::insertData(int total){
    for(int i=1;i<=total;i++){
        cout<<endl<<"Enter Marks: ";
        cin>>mks[i];
        int j=i;
        int par = j/2;
        
        while(mks[j]<mks[par] && j!=0){
            int temp = mks[j];
            mks[j] = mks[par];
            mks[par] = temp;
            
            j= par;
            par = j/2;
        }
    }
}

void stud::minMarks(){
    cout<<endl<<"Min Marks: "<<mks[1];
}
 void stud::maxMarks(int total){
    int max1 = mks[1];
    for(int i=2 ; i<=total ; i++){
        if(max1 < mks[i]){
            max1 = mks[i];
        }
    }
    cout<<endl<<"Max Marks: "<<max1;
 }

void stud::displayHeap(int total){
    int i=1 , space =6;
    cout<<endl;

    while(i<=total){
        if(i==1 || i==2 || i==4 || i==8 || i==16){
            cout<<endl<<endl;
            for(int j=0 ; j<space ; j++){
                cout<<" ";
            }
            space -= 2;
        }
        cout<<" "<<mks[i];
        i++;
    }
}

int main() {
    int ch,cont,total;
    stud s1;
    do{
        cout<<"Menu\n1.Insert Data\n2.Min Marks\n3.Max Marks\n4.Display Min-Heap"<<endl;
        cin>>ch;
        switch(ch){
            case 1:
                cout<<endl<<"How many records";
                cin>>total;
                s1.insertData(total);
                break;
            case 2:
                s1.minMarks();
                break;
            case 3:
                s1.maxMarks(total);
                break;
            case 4:
                s1.displayHeap(total);
                break;
        }
        cout<<endl<<"Do you want to continue (1): ";
        cin>>cont;
    }while(cont == 1);

    return 0;
}
