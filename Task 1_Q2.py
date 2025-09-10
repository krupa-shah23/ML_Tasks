def function(runes)
    gotl=gotu=gotm=goto=gots=False;

for i,r in loop (runes,1)
{
    r=r.upper();
    if(r==L):
        gotl=True;
    if(r==U):
        gotu=True;
    if(r==M):
        gotm=True;
    if(r==O):
        goto=True;
    if(r==S):
        gots=True;

     if gotL and gotU and gotM and gotO and gotS:
        return i;
    
    

}