python network/scale_trace.py --trace-in network/traces/cellular/Verizon1.dat --trace-out /tmp/scaled2/verizon1.txt --target-mbps=2

python network/scale_trace.py --trace-in network/traces/cellular/Verizon2.dat --trace-out /tmp/scaled2/verizon2.txt --target-mbps=2

python network/scale_trace.py --trace-in network/traces/cellular/ATT1.dat --trace-out /tmp/scaled2/Att1.txt --target-mbps=2

python network/scale_trace.py --trace-in network/traces/cellular/ATT2.dat --trace-out /tmp/scaled2/Att2.txt --target-mbps=2

python network/scale_trace.py --trace-in network/traces/cellular/TMobile1.dat --trace-out /tmp/scaled2/TMobile1.txt --target-mbps=2

python network/scale_trace.py --trace-in network/traces/cellular/TMobile2.dat --trace-out /tmp/scaled2/TMobile2.txt --target-mbps=2



python sim/run_exp.py -- --mm-trace=/tmp/scaled2/verizon1.txt --results-dir=results/scaled2/verizon1Results

python sim/run_exp.py -- --mm-trace=/tmp/scaled2/verizon2.txt --results-dir=results/scaled2/verizon2Results

python sim/run_exp.py -- --mm-trace=/tmp/scaled2/Att1.txt --results-dir=results/scaled2/Att1Results 

python sim/run_exp.py -- --mm-trace=/tmp/scaled2/Att2.txt --results-dir=results/scaled2/Att2Results

python sim/run_exp.py -- --mm-trace=/tmp/scaled2/TMobile1.txt --results-dir=results/scaled2/TMobile1Results

python sim/run_exp.py -- --mm-trace=/tmp/scaled2/TMobile2.txt --results-dir=results/scaled2/TMobile2Results
