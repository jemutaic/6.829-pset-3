python network/scale_trace.py --trace-in network/traces/cellular/Verizon1.dat --trace-out /tmp/scaled1/verizon1.txt --target-mbps=1

python network/scale_trace.py --trace-in network/traces/cellular/Verizon2.dat --trace-out /tmp/scaled1/verizon2.txt --target-mbps=1

python network/scale_trace.py --trace-in network/traces/cellular/ATT1.dat --trace-out /tmp/scaled1/Att1.txt --target-mbps=1

python network/scale_trace.py --trace-in network/traces/cellular/ATT2.dat --trace-out /tmp/scaled1/Att2.txt --target-mbps=1

python network/scale_trace.py --trace-in network/traces/cellular/TMobile1.dat --trace-out /tmp/scaled1/TMobile1.txt --target-mbps=1

python network/scale_trace.py --trace-in network/traces/cellular/TMobile2.dat --trace-out /tmp/scaled1/TMobile2.txt --target-mbps=1



python sim/run_exp.py -- --mm-trace=/tmp/scaled1/verizon1.txt --results-dir=results/verizon1Results

python sim/run_exp.py -- --mm-trace=/tmp/scaled1/verizon2.txt --results-dir=results/verizon2Results

python sim/run_exp.py -- --mm-trace=/tmp/scaled1/Att1.txt --results-dir=results/Att1Results 

python sim/run_exp.py -- --mm-trace=/tmp/scaled1/Att2.txt --results-dir=results/Att2Results

python sim/run_exp.py -- --mm-trace=/tmp/scaled1/TMobile1.txt --results-dir=results/TMobile1Results

python sim/run_exp.py -- --mm-trace=/tmp/scaled1/TMobile2.txt --results-dir=results/TMobile2Results