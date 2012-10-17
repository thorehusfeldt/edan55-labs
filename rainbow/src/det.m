function [d]=det(A,p)
  n=size(A,1);
  d=1;
  rs=zeros(1,n);	
  for i=1:n,
    who=-1;
    for j=1:n,
      if rs(j)==0 && A(j,i)~=0,
        rs(j) = i;
        who = j;
        d = mod(d*A(j,i),p);
        break;
      end;
    end;
    if who==-1,
      d = 0;
      break;
    end;
    for j=1:n,
      if (rs(j)==0 && A(j,i)~=0)
        d=mod(d*modexp(A(who,i),p-2,p), p);
        A(j,:) = mod(A(who,i)*A(j,:)-A(j,i)*A(who,:),p);
      end;
    end;
  end;
  if (d>0),
    sgn = n;
    vis=zeros(1,n);
    for i=1:n,
      if vis(i)==0,
        j=i;
        sgn=sgn-1;
        while (vis(j)==0),
          vis(j) = 1;
          j=rs(j);
         end;
      end;
    end;
    if (mod(sgn,2)==1),
      d=p-d;
    end;		
  end
end

function [r]=modexp(a,e,p)
  if (e==1)
    r = a;
  else 
    r = modexp(a,floor(e/2),p);
    r = mod(r*r,p);
    if (mod(e,2)==1)
      r = mod(r*a,p);
    end
  end
end