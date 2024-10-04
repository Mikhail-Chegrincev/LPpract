def f(x1,x2,x3,y1,y2,y3,z1,z2,z3,t1,t2,t3):
    xy = ((x1-y1)**2+(x2-y2)**2+(x3-y3)**2)**0.5
    xz = ((x1-z1)**2+(x2-z2)**2+(x3-z3)**2)**0.5
    xt = ((x1-t1)**2+(x2-t2)**2+(x3-t3)**2)**0.5
    zy = ((z1-y1)**2+(z2-y2)**2+(z3-y3)**2)**0.5
    ty = ((t1-y1)**2+(t2-y2)**2+(t3-y3)**2)**0.5
    zt = ((z1-t1)**2+(z2-t2)**2+(z3-t3)**2)**0.5
    return min(xy,xz,xt,zy,ty,zt)
print(f(int(input()),int(input()),int(input()),int(input()),int(input()),int(input()),\
        int(input()),int(input()),int(input()),int(input()),int(input()),int(input())))