#part one, 515
cat input.txt | awk -F'[-,]' '{print $1, $2, $3, $4}' | xargs -l bash -c 'echo $(seq -f \"%.1f\" -s "," $0 $1):$(seq -f \"%.1f\" -s "," $2 $3)' | awk -F : '{ sum += ($1 ~ $2 || $2 ~ $1)} END { print sum}'

#part two, 883
cat input.txt | awk -F'[-,]' '{print $1, $2, $3, $4}' | xargs -l bash -c '(seq $0 $1; seq $2 $3) | sort | uniq -d | paste -s -d ""' | sed '/^\s*$/d' | wc -l

