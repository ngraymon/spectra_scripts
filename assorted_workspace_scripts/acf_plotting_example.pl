set terminal png size 1200,800
set title 'ACF comparison of 25fs'
set style line 1 lt 2 pt 12 ps 1 pi -1
set style data line
set output './ACF_hexahelicene_vibronic_linear_4000_25fs.png'
set nologscale
set xzeroaxis
set ylabel 'C(tau/hbar)'
set yr [ -1: 1]
set xr [ 0.0: 25.0]
plot \
    '$WORK_DIR/hexahelicene/hexahelicene_vibronic_linear_tf25.00/ACF_ABS_CC_hexahelicene_vibronic_linear_tf25_normalized.txt' \
        using 1:2 lc 'green' title 'CC Real (interpolated)', \
    '$WORK_DIR/hexahelicene/hexahelicene_vibronic_linear_tf25.00/ACF_ABS_CC_hexahelicene_vibronic_linear_tf25.txt' \
        using 1:2 with linespoints ls 1 lc 'blue' title 'CC Real (raw RK45)', \