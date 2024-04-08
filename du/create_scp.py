import os

train_mix_scp = './create_scp/tr_mix.scp'
train_s1_scp = './create_scp/tr_s1.scp'
train_s2_scp = './create_scp/tr_s2.scp'

test_mix_scp = './create_scp/tt_mix.scp'
test_s1_scp = './create_scp/tt_s1.scp'
test_s2_scp = './create_scp/tt_s2.scp'

cv_mix_scp = './create_scp/cv_mix.scp'
cv_s1_scp = './create_scp/cv_s1.scp'
cv_s2_scp = './create_scp/cv_s2.scp'

cv_mix = '../skdata/dev-clean/data8000/s'
cv_s1 = '../skdata/dev-clean/data8000/s'
cv_s2 = '../skdata/dev-clean/data8000/s'

train_mix = '../skdata/train-clean-100/data8000/s'
train_s1 = '../skdata/train-clean-100/data8000/s'
train_s2 = '../skdata/train-clean-100/data8000/s'

test_mix = '../skdata/test-clean/data8000/s'
test_s1 = '../skdata/test-clean/data8000/s'
test_s2 = '../skdata/test-clean/data8000/s'
def s_c_scp(scp,path,fname,inum): 
    op = open(scp,'w')
    for root, dirs, f in os.walk(path):
        i=inum
        for dir in dirs:
            op.write(dir+fname+" "+root+'/'+dir+'/'+fname)
            op.write('\n')
            i-=1
            if i==0:
                return
if not os.path.exists('./create_scp'):
    os.makedirs('./create_scp')
s_c_scp(train_mix_scp,train_mix,'mix.wav',20)
s_c_scp(train_s1_scp,train_s1,'sk1.wav',20)
s_c_scp(train_s2_scp,train_s2,'sk2.wav',20)
s_c_scp(test_mix_scp,test_mix,'mix.wav',4)
s_c_scp(test_s1_scp,test_s1,'sk1.wav',4)
s_c_scp(test_s2_scp,test_s2,'sk2.wav',4)
s_c_scp(cv_mix_scp,cv_mix,'mix.wav',4)
s_c_scp(cv_s1_scp,cv_s1,'sk1.wav',4)
s_c_scp(cv_s2_scp,cv_s2,'sk2.wav',4)