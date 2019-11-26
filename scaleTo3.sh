python network/scale_trace.py --trace-in network/traces/cellular/Verizon1.dat --trace-out /tmp/scaled3/verizon1.txt --target-mbps=3

python network/scale_trace.py --trace-in network/traces/cellular/Verizon2.dat --trace-out /tmp/scaled3/verizon2.txt --target-mbps=3

python network/scale_trace.py --trace-in network/traces/cellular/ATT1.dat --trace-out /tmp/scaled3/Att1.txt --target-mbps=3

python network/scale_trace.py --trace-in network/traces/cellular/ATT2.dat --trace-out /tmp/scaled3/Att2.txt --target-mbps=3

python network/scale_trace.py --trace-in network/traces/cellular/TMobile1.dat --trace-out /tmp/scaled3/TMobile1.txt --target-mbps=3

python network/scale_trace.py --trace-in network/traces/cellular/TMobile2.dat --trace-out /tmp/scaled3/TMobile2.txt --target-mbps=3



python sim/run_exp.py -- --mm-trace=/tmp/scaled3/verizon1.txt --results-dir=results/scaled3/verizon1Results

python sim/run_exp.py -- --mm-trace=/tmp/scaled3/verizon2.txt --results-dir=results/scaled3/verizon2Results

python sim/run_exp.py -- --mm-trace=/tmp/scaled3/Att1.txt --results-dir=results/scaled3/Att1Results 

python sim/run_exp.py -- --mm-trace=/tmp/scaled3/Att2.txt --results-dir=results/scaled3/Att2Results

python sim/run_exp.py -- --mm-trace=/tmp/scaled3/TMobile1.txt --results-dir=results/scaled3/TMobile1Results

python sim/run_exp.py -- --mm-trace=/tmp/scaled3/TMobile2.txt --results-dir=results/scaled3/TMobile2Results
