#include<iostream>
#include<fstream>
#include<cstdio>
#include<string.h>
#include<sstream>
#include<stdlib.h>
using namespace std;
int charToInt (char _char);
int stringToInteger(string str);
int Power(int base,int power);
void WriteInFile(string InFile);
string numberToString(int num );
int main(){
	fstream File_Position("SendToCPlus.txt",ios::in);
	if(!File_Position){
		cerr<<"File Can Not Open!"<<endl;
		exit(1);}
	string File_Contain,First,Second,Operator;
	while(File_Position>>File_Contain);
	int counter=0;
	while(true){
		if(atoi(&File_Contain[counter]))
			First += File_Contain[counter];
		else if(File_Contain[counter]=='|')
		 	break;
		counter++;
	}
	counter++;
	while(true){
		if(atoi(&File_Contain[counter]))
			Second += File_Contain[counter];
		else if(File_Contain[counter]=='|')
		 	break;
		counter++;
	}
	Operator=File_Contain[++counter];
	//cout<<First<<endl<<Second<<endl<<Operator;
	int _First = stringToInteger(First);
	int _Second = stringToInteger(Second);
	if(Operator=="+"){
		string a = numberToString(_First+_Second);
		WriteInFile(a);}
	else if(Operator=="-"){
		string a = numberToString(_First-_Second);
		//cout<<a;
		WriteInFile(a);}	
	else if(Operator=="*"){
		string a = numberToString(_First*_Second);
		WriteInFile(a);}	
	else if(Operator=="/"){
		string a = numberToString(_First/_Second);
		WriteInFile(a);}
	else if(Operator=="^"){
		string a = numberToString(Power(_First,_Second));
		WriteInFile(a);}		
	return 0;
}
int charToInt (char _char){
    for (int i = 48, num = 0; i < 58; i++, num++)
    if ((int)_char == i)
        return num;
}
int stringToInteger(string str)
{
    int result;
    istringstream convert(str);
    if ( !(convert >> result) )
       throw "Can not convert";
 
    return result;
}
void WriteInFile(string InFile){
	fstream Output_File("SendToCSharp.txt",ios::out);
	if(!Output_File){
		cerr<<"File Can Not Open!"<<endl;
		exit(1);}
	Output_File<<InFile;	
}
int Power(int base,int power){
	if(power >1){
		return (base*(Power(base,power-1)));
	}
	else
		return base;
		
}
string numberToString(int num )  
{   ostringstream os;  
    os << num;      
    return os.str(); 
} 
