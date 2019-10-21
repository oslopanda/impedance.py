from impedance.preprocessing import readFile, readGamry, ignoreBelowX
from impedance.preprocessing import readZPlot, readVersaStudio
from impedance.preprocessing import cropFrequencies
import numpy as np

# store some global test data
frequencies = np.array([0.0031623, 0.0039811, 0.0050119, 0.0063096,
                        0.0079433, 0.01, 0.012589, 0.015849, 0.019953,
                        0.025119, 0.031623, 0.039811, 0.050119, 0.063096,
                        0.079433, 0.1, 0.12589, 0.15849, 0.19953, 0.25119,
                        0.31623, 0.39811, 0.50119, 0.63096, 0.79433, 1.0,
                        1.2589, 1.5849, 1.9953, 2.5119, 3.1623, 3.9811,
                        5.0119, 6.3096, 7.9433, 10.0, 12.589, 15.849,
                        19.953, 25.119, 31.623, 39.811, 50.119, 63.096,
                        79.433, 100.0, 125.89, 158.49, 199.53, 251.19,
                        316.23, 398.11, 501.19, 630.96, 794.33, 1000.0,
                        1258.9, 1584.9, 1995.3, 2511.9, 3162.3, 3981.1,
                        5011.9, 6309.6, 7943.3, 10000.0])

real = [0.0494998977640506, 0.04776559257398882, 0.04613581757142157,
        0.044596836301773274, 0.043142303861239205, 0.04181678802099761,
        0.040606740929859095, 0.03951932383144551, 0.03856629404354767,
        0.03773445890891119, 0.037013908851197805, 0.03639992299924442,
        0.035883179203561086, 0.03544780816944048, 0.03506693121253139,
        0.034721707243418394, 0.03440366308110683, 0.03410783765793668,
        0.033821109172144787, 0.03353616639243526, 0.0332524554516705,
        0.03295910966053001, 0.03265642728210896, 0.03232796211965539,
        0.03197349380289498, 0.03158436174556338, 0.031069936132208306,
        0.030461419854177326, 0.029900714166654168, 0.029379111339927506,
        0.028614488514401064, 0.027877380810968015, 0.027051941695755265,
        0.02622642987302172, 0.02539677675995668, 0.024674033206038913,
        0.023984220630662276, 0.023376189861574193, 0.022795788586331325,
        0.022290491192888506, 0.02183347892172112, 0.021423948245372654,
        0.021044983846558948, 0.02061274834162727, 0.02020959510042839,
        0.019760492004316906, 0.019397188854563818, 0.01898347057349932,
        0.018562859805406066, 0.018173948838613962, 0.017777098024495532,
        0.017382944047369668, 0.017027408256891644, 0.016664493440403796,
        0.016338702344109557, 0.0160611742499297, 0.01580888106340524,
        0.015584763288620133, 0.015355525008021014, 0.0151995284094296,
        0.015171093447136087, 0.0151260119032158, 0.015086882844244285,
        0.015276246310902308, 0.015467639396989145, 0.015771482660485933]

imag = [-0.020438698544418925, -0.0182856893045487, -0.016343158966700824,
        -0.014589168660649915, -0.01300096361736358, -0.011573009182824043,
        -0.010282133623145187, -0.009113366697002839, -0.00804494958277692,
        -0.007075702921918925, -0.006209940124316647, -0.005450664199993216,
        -0.004804611324614652, -0.0042630212172992624, -0.003816723014957778,
        -0.003465230467686932, -0.0031936182833490197, -0.0029843274850640607,
        -0.0028420187384119175, -0.0027510821389620833, -0.0027092774650327093,
        -0.002716402585530142, -0.0027688021541761596, -0.0028687505233332576,
        -0.002995332546857452, -0.0031633863009665544, -0.0034345232421858604,
        -0.003652697342055591, -0.00389594513544332, -0.0041496368125138496,
        -0.0043563647278047945, -0.004528514961203703, -0.004623972802104744,
        -0.00463483440841946, -0.004562544489738368, -0.0044183840649258165,
        -0.004213943600562558, -0.00397620055979716, -0.0037290248504921668,
        -0.0035578892246933775, -0.0033509582749051627, -0.0031826464281827804,
        -0.0030507184111723995, -0.0029386920239828154, -0.002848034411523496,
        -0.0027583877127425357, -0.0026767011351060705, -0.002575856490231119,
        -0.002455805016755156, -0.0023163152672671405, -0.002149498808757098,
        -0.0019492643145405137, -0.0017151675874650793, -0.0014357936694323731,
        -0.001109438368794195, -0.0007287022309982213, -0.0002827724289657194,
        0.00024224721030238663, 0.0008560734952241664, 0.0015811469785105114,
        0.002452846099159856, 0.003488131035300228, 0.004712940823286973,
        0.006239444322658155, 0.008031686651315248, 0.010157474564938236]

imag_np = [-0.020438698544418925,
           -0.0182856893045487,
           -0.016343158966700824,
           -0.014589168660649915,
           -0.01300096361736358,
           -0.011573009182824043,
           -0.010282133623145187,
           -0.009113366697002839,
           -0.00804494958277692,
           -0.007075702921918925,
           -0.006209940124316647,
           -0.005450664199993216,
           -0.004804611324614652,
           -0.0042630212172992624,
           -0.003816723014957778,
           -0.003465230467686932,
           -0.0031936182833490197,
           -0.0029843274850640607,
           -0.0028420187384119175,
           -0.0027510821389620833,
           -0.0027092774650327093,
           -0.002716402585530142,
           -0.0027688021541761596,
           -0.0028687505233332576,
           -0.002995332546857452,
           -0.0031633863009665544,
           -0.0034345232421858604,
           -0.003652697342055591,
           -0.00389594513544332,
           -0.0041496368125138496,
           -0.0043563647278047945,
           -0.004528514961203703,
           -0.004623972802104744,
           -0.00463483440841946,
           -0.004562544489738368,
           -0.0044183840649258165,
           -0.004213943600562558,
           -0.00397620055979716,
           -0.0037290248504921668,
           -0.0035578892246933775,
           -0.0033509582749051627,
           -0.0031826464281827804,
           -0.0030507184111723995,
           -0.0029386920239828154,
           -0.002848034411523496,
           -0.0027583877127425357,
           -0.0026767011351060705,
           -0.002575856490231119,
           -0.002455805016755156,
           -0.0023163152672671405,
           -0.002149498808757098,
           -0.0019492643145405137,
           -0.0017151675874650793,
           -0.0014357936694323731,
           -0.001109438368794195,
           -0.0007287022309982213,
           -0.0002827724289657194]

Z_correct = np.array(real) + 1j*np.array(imag)

f_gamry = np.array([2.000156e+05, 1.589531e+05, 1.262344e+05, 1.002656e+05,
                    7.964063e+04, 6.332812e+04, 5.029688e+04, 3.998437e+04,
                    3.173438e+04, 2.526563e+04, 2.001562e+04, 1.589062e+04,
                    1.270313e+04, 1.007813e+04, 8.015625e+03, 6.328125e+03,
                    5.009191e+03, 3.998162e+03, 3.170956e+03, 2.527573e+03,
                    2.015625e+03, 1.577524e+03, 1.265625e+03, 9.982640e+02,
                    7.968750e+02, 6.277902e+02, 5.055147e+02, 3.979953e+02,
                    3.155048e+02, 2.524038e+02, 1.986229e+02, 1.583615e+02,
                    1.255580e+02, 1.004464e+02, 7.990057e+01, 6.334460e+01,
                    4.986702e+01, 3.972458e+01, 3.167230e+01, 2.493351e+01,
                    1.986229e+01, 1.583615e+01, 1.240079e+01, 9.931140e+00,
                    7.944915e+00, 6.317385e+00, 5.008013e+00, 4.020154e+00,
                    3.158693e+00, 2.504006e+00, 1.998082e+00, 1.584686e+00,
                    1.266892e+00, 9.990410e-01, 7.923428e-01, 6.334460e-01,
                    5.040323e-01, 4.006410e-01, 3.188775e-01, 2.520161e-01,
                    2.003205e-01, 1.588983e-01, 1.263477e-01, 1.003747e-01,
                    7.971940e-02, 6.325910e-02, 5.024120e-02, 3.992760e-02,
                    3.171520e-02, 2.518810e-02, 2.000640e-02, 1.588980e-02])

Zr_gamry = np.array([825.8584, 1100.361, 1401.721, 1739.625, 2087.403,
                     2422.298, 2720.257, 2982.016, 3212.336, 3359.629,
                     3499.298, 3598.306, 3688.117, 3766.628, 3808.92,
                     3842.264, 3902.565, 3927.298, 3944.01, 3987.966,
                     3998.507, 4029.045, 4044.939, 4077.349, 4068.979,
                     4072.986, 4078.837, 4107.241, 4130.96, 4143.088,
                     4164.664, 4183.986, 4206.823, 4225.685, 4230.309,
                     4228.707, 4242.562, 4250.716, 4219.722, 4208.409,
                     4203.486, 4213.595, 4241.487, 4258.891, 4295.819,
                     4297.472, 4313.771, 4361.165, 4408.525, 4430.184,
                     4495.299, 4571.314, 4632.138, 4753.051, 4889.047,
                     5038.293, 5218.515, 5444.164, 5926.305, 6461.792,
                     7343.626, 7986.202, 8435.127, 8973.929, 10123.93,
                     10823.63, 11628.01, 12514.52, 13482.75, 14713.85,
                     15701.81, 17007.49])

Zi_gamry = np.array([-1367.239, -1502.195, -1621.813, -1672.93, -1668.395,
                     -1620.144, -1506.859, -1407.856, -1266.296, -1091.802,
                     -947.1432, -813.0331, -704.9116, -606.206, -516.6904,
                     -439.2898, -382.0586, -327.8677, -279.8773, -247.0336,
                     -214.7129, -187.785, -163.6504, -146.0875, -128.724,
                     -114.1715, -105.0351, -95.6213, -88.8763, -82.36904,
                     -77.56557, -73.49171, -70.95162, -68.13791, -69.87909,
                     -68.70265, -73.79854, -78.35508, -81.94554, -94.86475,
                     -104.9407, -122.1189, -142.8908, -164.5738, -195.5508,
                     -228.205, -275.2808, -321.6813, -387.5287, -470.5144,
                     -558.4168, -655.9384, -773.8778, -913.8754, -1069.582,
                     -1243.894, -1440.5, -1644.846, -1891.697, -2170.397,
                     -2427.713, -2737.648, -3059.258, -3423.424, -3800.406,
                     -4165.968, -4477.789, -4931.03, -5301.367, -5703.416,
                     -6161.72, -6635.557])

Z_gamry = Zr_gamry + 1j*Zi_gamry

f_VerStu = np.array([100000, 77426.37, 59948.43, 46415.89, 35938.14,
                    27825.59, 21544.35, 16681.01, 12915.5, 10000, 7742.637,
                    5994.842, 4641.589, 3593.814, 2782.559, 2154.435, 1668.101,
                    1291.55, 1000, 774.2637, 599.4843, 464.1589, 359.3814,
                    278.256, 215.4435, 166.8101, 129.155, 100, 77.42637,
                    59.94843, 46.41589, 35.93814, 27.82559, 21.54435,
                    16.68101, 12.9155, 10, 7.742637, 5.994843, 4.641589,
                    3.593814, 2.782559, 2.154435, 1.668101, 1.29155, 1,
                    0.7742637, 0.5994843, 0.4641589, 0.3593814, 0.2782559,
                    0.2154435, 0.1668101, 0.129155, 0.1, 0.07742637,
                    0.05994843, 0.04641589, 0.03593814, 0.02782559,
                    0.02154435])

Zr_VerStu = np.array([55.31571, 56.93847, 58.32154, 59.73283, 60.96293,
                      62.34844, 63.46056, 64.4969, 65.37202, 66.43731,
                      67.78217, 68.5193, 69.38809, 70.42213, 72.07207,
                      73.06129, 73.40866, 74.38404, 74.87874, 75.47595,
                      76.09173, 76.62376, 77.23329, 77.31622, 77.82825,
                      79.15672, 80.31376, 81.37247, 82.76803, 85.77745,
                      87.94788, 91.79543, 96.59234, 103.7106, 114.1878,
                      124.8123, 139.6575, 160.5535, 184.8712, 216.3164,
                      254.2599, 299.4102, 352.4197, 413.7206, 482.5668,
                      558.9164, 639.3323, 727.537, 820.1124, 915.3231,
                      1010.121, 1105.063, 1186.953, 1263.267, 1328.254,
                      1382.254, 1424.577, 1453.814, 1481.78, 1502.032,
                      1516.313])

Zi_VerStu = np.array([4.575431, 1.668054, -0.03684627, -1.969503, -2.897054,
                     -3.826518, -4.245813, -4.721501, -4.980665, -5.291955,
                     -5.316875, -5.578281, -5.477057, -5.731471, -5.816343,
                     -5.628813, -5.913171, -6.051136, -6.137753, -6.528912,
                     -7.033413, -7.800642, -8.996423, -10.57455, -12.52785,
                     -15.52149, -19.00842, -23.22614, -29.20773, -34.91376,
                     -43.38998, -53.83748, -66.16342, -81.11567, -99.15878,
                     -119.0632, -141.2555, -169.2192, -198.209, -230.7009,
                     -264.5615, -299.5144, -335.2198, -370.0366, -400.9045,
                     -429.04, -451.8962, -468.4555, -478.3702, -478.1073,
                     -469.5371, -449.1746, -420.9942, -384.3542, -342.7299,
                     -299.3539, -257.4971, -215.6761, -181.6588, -150.2267,
                     -122.8279])

Z_VerStu = Zr_VerStu + 1j * Zi_VerStu


f_ZPlot = np.array([3.000000e+05, 2.382985e+05, 1.892872e+05, 1.503562e+05,
                    1.194321e+05, 9.486833e+04, 7.535659e+04, 5.985787e+04,
                    4.754680e+04, 3.776776e+04, 3.000000e+04, 2.382985e+04,
                    1.892872e+04, 1.503562e+04, 1.194321e+04, 9.486833e+03,
                    7.535659e+03, 5.985787e+03, 4.754680e+03, 3.776776e+03,
                    3.000000e+03, 2.382985e+03, 1.892872e+03, 1.503562e+03,
                    1.194322e+03, 9.486833e+02, 7.535659e+02, 5.985787e+02,
                    4.754680e+02, 3.776776e+02, 3.000000e+02, 2.382985e+02,
                    1.892872e+02, 1.503562e+02, 1.194322e+02, 9.486833e+01,
                    7.535659e+01, 5.985787e+01, 4.754680e+01, 3.776776e+01,
                    3.000000e+01, 2.382985e+01, 1.892872e+01, 1.503562e+01,
                    1.194322e+01, 9.486830e+00, 7.535660e+00, 5.985790e+00,
                    4.754680e+00, 3.776780e+00, 3.000000e+00, 2.382980e+00,
                    1.892870e+00, 1.503560e+00, 1.194320e+00, 1.000000e+00])

Zr_ZPlot = np.array([147.77, 148.93, 150.48, 151.46, 153.2, 155.62, 158.98,
                    164.45, 172.73, 184.99, 203.10, 228.85, 264.03, 309.13,
                    362.59, 419.55, 475.02, 523.25, 563.36, 590.31, 613.68,
                    626.31, 635.67, 641.11, 645.33, 648.19, 649.75, 650.67,
                    652.12, 651.82, 653.25, 652.64, 652.37, 653.05, 651.39,
                    653.11, 652.42, 654.90, 653.10, 653.17, 653.14, 653.53,
                    652.66, 653.13, 652.79, 652.05, 653.44, 651.58, 650.93,
                    653.24, 654.68, 652.33, 652.27, 652.48, 653.25, 654.19])

Zi_ZPlot = np.array([-1.1335e+01, -1.7302e+01, -2.3653e+01, -3.1301e+01,
                    -4.0748e+01, -5.2177e+01, -6.5761e+01, -8.2536e+01,
                    -1.0261e+02, -1.2607e+02, -1.5276e+02, -1.8117e+02,
                    -2.0876e+02, -2.3205e+02, -2.4704e+02, -2.4885e+02,
                    -2.3945e+02, -2.1885e+02, -1.9176e+02, -1.6694e+02,
                    -1.3713e+02, -1.1137e+02, -9.0614e+01, -7.1190e+01,
                    -5.9297e+01, -4.6257e+01, -3.6456e+01, -3.0742e+01,
                    -2.3792e+01, -1.8864e+01, -1.2276e+01, -1.1308e+01,
                    -9.5142e+00, -7.6985e+00, -6.3635e+00, -4.9270e+00,
                    -4.3839e+00, -1.4622e+00, -2.0900e+00, -1.8532e+00,
                    -1.7382e+00, -1.4767e+00, -8.4596e-01, -1.3005e+00,
                    -1.1834e+00, -1.1508e+00, -8.3833e-01, -7.0630e-01,
                    8.1795e-02, 6.2940e-01, 1.6343e-01,  5.4773e-01,
                    -5.1657e-01,  1.6725e+00, -1.2792e-01,  6.4271e-01])

Z_ZPlot = Zr_ZPlot + 1j * Zi_ZPlot


def test_readFile():

    f, Z = readFile('./data/exampleData.csv')

    assert (f == frequencies).all() and (Z == Z_correct).all()


def test_readGamry():

    f, Z = readGamry('./data/Chalco-in-buffer-50mV.DTA')

    assert (f == f_gamry).all() and (Z == Z_gamry).all()


def test_readVersaStudio():

    f, Z = readVersaStudio('./data/exampleDataVersaStudio.par')

    assert (f == f_VerStu).all() and (Z == Z_VerStu).all()


def test_readZPlot():

    f, Z = readZPlot('./data/exampleDataZPlot.z')

    assert (f == f_ZPlot).all() and (Z == Z_ZPlot).all()


def test_ignoreBelowX():

    filtered_freq, filtered_Z = ignoreBelowX(frequencies, Z_correct)

    assert (np.imag(filtered_Z) == imag_np).all()


def test_cropFreq_maxonly():

    filtered_freq, filtered_Z = cropFrequencies(frequencies, Z_correct,
                                                freqmax=1e3)

    assert (filtered_freq <= 1e3).all()


def test_cropFreq_minonly():

    filtered_freq, filtered_Z = cropFrequencies(frequencies, Z_correct,
                                                freqmin=1)

    assert (filtered_freq >= 1).all()


def test_cropFreq_both():

    filtered_freq, filtered_Z = cropFrequencies(frequencies, Z_correct,
                                                freqmin=1, freqmax=1e3)

    assert (filtered_freq >= 1).all() and (filtered_freq <= 1e3).all()
