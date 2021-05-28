fileName='白鹿原_雨枫轩Rain8.com.txt'

file=open(fileName,'r')

res=open('白鹿原.txt','w')

out=[];
lines=file.read().split('\n')
for (index,line) in enumerate(lines):
  if len(line)<1:
    continue
  if str(line)[-1]=='。':
    out.append(line+'\n')
  else:
    out.append(line)
    
print(''.join(out));
res.write(''.join(out))
file.close()
res.close()
