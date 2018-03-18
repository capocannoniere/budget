#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PYTHON=${PYTHON:-python}

REVISION1="2012-12-03"
REVISION2="2013-06-07"
REVISION3="2013-12-02"

# Main budget text
echo "Processing main budget text..."
"${PYTHON}" "${SCRIPT_DIR}/budget2013_0.py" \
	-i "${SCRIPT_DIR}/../doc/budget-${REVISION1}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/budget-${REVISION1}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/budget-${REVISION1}.txt" \
	--output-json "${SCRIPT_DIR}/../data/budget-${REVISION1}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/budget-${REVISION1}.pretty.json"
"${PYTHON}" "${SCRIPT_DIR}/budget2013_0.py" \
	-i "${SCRIPT_DIR}/../doc/budget-${REVISION2}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/budget-${REVISION2}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/budget-${REVISION2}.txt" \
	--output-json "${SCRIPT_DIR}/../data/budget-${REVISION2}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/budget-${REVISION2}.pretty.json"
"${PYTHON}" "${SCRIPT_DIR}/budget2013_0.py" \
	-i "${SCRIPT_DIR}/../doc/budget-${REVISION3}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/budget-${REVISION3}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/budget-${REVISION3}.txt" \
	--output-json "${SCRIPT_DIR}/../data/budget-${REVISION3}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/budget-${REVISION3}.pretty.json"

# Annex 1
echo "Processing annex 1..."
"${PYTHON}" "${SCRIPT_DIR}/budget2013_1.py" \
	-i "${SCRIPT_DIR}/../doc/annex01-${REVISION1}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex01-${REVISION1}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex01-${REVISION1}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex01-${REVISION1}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex01-${REVISION1}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex01-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex01-${REVISION2}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex01-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex01-${REVISION3}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex01-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex01-${REVISION2}.txt"
cp -f "${SCRIPT_DIR}/../data/annex01-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex01-${REVISION3}.txt"
cp -f "${SCRIPT_DIR}/../data/annex01-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex01-${REVISION2}.json"
cp -f "${SCRIPT_DIR}/../data/annex01-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex01-${REVISION3}.json"
cp -f "${SCRIPT_DIR}/../data/annex01-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex01-${REVISION2}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex01-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex01-${REVISION3}.pretty.json"

# Annex 2
echo "Processing annex 2..."
"${PYTHON}" "${SCRIPT_DIR}/budget2013_2.py" \
	-i "${SCRIPT_DIR}/../doc/annex02-${REVISION1}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex02-${REVISION1}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex02-${REVISION1}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex02-${REVISION1}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex02-${REVISION1}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex02-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex02-${REVISION2}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex02-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex02-${REVISION3}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex02-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex02-${REVISION2}.txt"
cp -f "${SCRIPT_DIR}/../data/annex02-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex02-${REVISION3}.txt"
cp -f "${SCRIPT_DIR}/../data/annex02-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex02-${REVISION2}.json"
cp -f "${SCRIPT_DIR}/../data/annex02-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex02-${REVISION3}.json"
cp -f "${SCRIPT_DIR}/../data/annex02-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex02-${REVISION2}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex02-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex02-${REVISION3}.pretty.json"

# Annex 3
echo "Processing annex 3..."
"${PYTHON}" "${SCRIPT_DIR}/budget2013_3.py" \
	-i "${SCRIPT_DIR}/../doc/annex03-${REVISION1}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex03-${REVISION1}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex03-${REVISION1}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex03-${REVISION1}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex03-${REVISION1}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex03-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex03-${REVISION2}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex03-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex03-${REVISION3}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex03-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex03-${REVISION2}.txt"
cp -f "${SCRIPT_DIR}/../data/annex03-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex03-${REVISION3}.txt"
cp -f "${SCRIPT_DIR}/../data/annex03-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex03-${REVISION2}.json"
cp -f "${SCRIPT_DIR}/../data/annex03-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex03-${REVISION3}.json"
cp -f "${SCRIPT_DIR}/../data/annex03-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex03-${REVISION2}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex03-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex03-${REVISION3}.pretty.json"

# Annex 4
echo "Processing annex 4..."
"${PYTHON}" "${SCRIPT_DIR}/budget2013_4.py" \
	-i "${SCRIPT_DIR}/../doc/annex04-${REVISION1}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex04-${REVISION1}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex04-${REVISION1}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex04-${REVISION1}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex04-${REVISION1}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex04-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex04-${REVISION2}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex04-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex04-${REVISION3}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex04-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex04-${REVISION2}.txt"
cp -f "${SCRIPT_DIR}/../data/annex04-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex04-${REVISION3}.txt"
cp -f "${SCRIPT_DIR}/../data/annex04-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex04-${REVISION2}.json"
cp -f "${SCRIPT_DIR}/../data/annex04-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex04-${REVISION3}.json"
cp -f "${SCRIPT_DIR}/../data/annex04-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex04-${REVISION2}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex04-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex04-${REVISION3}.pretty.json"

# Annex 5
echo "Processing annex 5..."
"${PYTHON}" "${SCRIPT_DIR}/budget2013_5.py" \
	-i "${SCRIPT_DIR}/../doc/annex05-${REVISION1}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex05-${REVISION1}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex05-${REVISION1}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex05-${REVISION1}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex05-${REVISION1}.pretty.json"
"${PYTHON}" "${SCRIPT_DIR}/budget2013_5.py" \
	-i "${SCRIPT_DIR}/../doc/annex05-${REVISION2}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex05-${REVISION2}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex05-${REVISION2}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex05-${REVISION2}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex05-${REVISION2}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex05-${REVISION2}.pkl" "${SCRIPT_DIR}/../data/annex05-${REVISION3}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex05-${REVISION2}.txt" "${SCRIPT_DIR}/../data/annex05-${REVISION3}.txt"
cp -f "${SCRIPT_DIR}/../data/annex05-${REVISION2}.json" "${SCRIPT_DIR}/../data/annex05-${REVISION3}.json"
cp -f "${SCRIPT_DIR}/../data/annex05-${REVISION2}.pretty.json" "${SCRIPT_DIR}/../data/annex05-${REVISION3}.pretty.json"

# Annex 6
echo "Processing annex 6..."
"${PYTHON}" "${SCRIPT_DIR}/budget2013_6.py" \
	-i "${SCRIPT_DIR}/../doc/annex06-${REVISION1}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex06-${REVISION1}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex06-${REVISION1}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex06-${REVISION1}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex06-${REVISION1}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex06-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex06-${REVISION2}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex06-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex06-${REVISION3}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex06-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex06-${REVISION2}.txt"
cp -f "${SCRIPT_DIR}/../data/annex06-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex06-${REVISION3}.txt"
cp -f "${SCRIPT_DIR}/../data/annex06-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex06-${REVISION2}.json"
cp -f "${SCRIPT_DIR}/../data/annex06-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex06-${REVISION3}.json"
cp -f "${SCRIPT_DIR}/../data/annex06-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex06-${REVISION2}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex06-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex06-${REVISION3}.pretty.json"

# Annex 7
echo "Processing annex 7..."
"${PYTHON}" "${SCRIPT_DIR}/budget2013_7.py" \
	-i "${SCRIPT_DIR}/../doc/annex07-${REVISION1}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex07-${REVISION1}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex07-${REVISION1}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex07-${REVISION1}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex07-${REVISION1}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex07-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex07-${REVISION2}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex07-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex07-${REVISION2}.txt"
cp -f "${SCRIPT_DIR}/../data/annex07-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex07-${REVISION2}.json"
cp -f "${SCRIPT_DIR}/../data/annex07-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex07-${REVISION2}.pretty.json"
"${PYTHON}" "${SCRIPT_DIR}/budget2013_7.py" \
	-i "${SCRIPT_DIR}/../doc/annex07-${REVISION3}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex07-${REVISION3}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex07-${REVISION3}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex07-${REVISION3}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex07-${REVISION3}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex07-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex07-combined-${REVISION1}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex07-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex07-combined-${REVISION1}.txt"
cp -f "${SCRIPT_DIR}/../data/annex07-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex07-combined-${REVISION1}.json"
cp -f "${SCRIPT_DIR}/../data/annex07-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex07-combined-${REVISION1}.pretty.json"

# Annex 7.1
echo "Processing annex 7.1..."
"${PYTHON}" "${SCRIPT_DIR}/budget2013_7_1.py" \
	-m "${SCRIPT_DIR}/../doc/annex07-${REVISION1}.txt" \
	-i "${SCRIPT_DIR}/../doc/annex07.1-${REVISION2}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex07.1-${REVISION2}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex07.1-${REVISION2}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex07.1-${REVISION2}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex07.1-${REVISION2}.pretty.json" \
	--combined-output-pickle "${SCRIPT_DIR}/../data/annex07-combined-${REVISION2}.pkl" \
	--combined-output-text "${SCRIPT_DIR}/../data/annex07-combined-${REVISION2}.txt" \
	--combined-output-json "${SCRIPT_DIR}/../data/annex07-combined-${REVISION2}.json" \
	--combined-output-json-pretty "${SCRIPT_DIR}/../data/annex07-combined-${REVISION2}.pretty.json"
"${PYTHON}" "${SCRIPT_DIR}/budget2013_7_1.py" \
	-m "${SCRIPT_DIR}/../doc/annex07-${REVISION3}.txt" \
	-i "${SCRIPT_DIR}/../doc/annex07.1-${REVISION2}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex07.1-${REVISION3}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex07.1-${REVISION3}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex07.1-${REVISION3}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex07.1-${REVISION3}.pretty.json" \
	--combined-output-pickle "${SCRIPT_DIR}/../data/annex07-combined-${REVISION3}.pkl.tmp"

# Annex 7.2
echo "Processing annex 7.2..."
"${PYTHON}" "${SCRIPT_DIR}/budget2013_7_2.py" \
	-m "${SCRIPT_DIR}/../data/annex07-combined-${REVISION3}.pkl.tmp" \
	-i "${SCRIPT_DIR}/../doc/annex07.2-${REVISION3}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex07.2-${REVISION3}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex07.2-${REVISION3}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex07.2-${REVISION3}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex07.2-${REVISION3}.pretty.json" \
	--combined-output-pickle "${SCRIPT_DIR}/../data/annex07-combined-${REVISION3}.pkl" \
	--combined-output-text "${SCRIPT_DIR}/../data/annex07-combined-${REVISION3}.txt" \
	--combined-output-json "${SCRIPT_DIR}/../data/annex07-combined-${REVISION3}.json" \
	--combined-output-json-pretty "${SCRIPT_DIR}/../data/annex07-combined-${REVISION3}.pretty.json"

rm -f "${SCRIPT_DIR}/../data/annex07-combined-${REVISION3}.pkl.tmp"

# Annex 10
echo "Processing annex 10..."
"${PYTHON}" "${SCRIPT_DIR}/budget2013_10.py" \
	-i "${SCRIPT_DIR}/../doc/annex10-${REVISION1}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex10-${REVISION1}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex10-${REVISION1}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex10-${REVISION1}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex10-${REVISION1}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex10-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex10-${REVISION2}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex10-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex10-${REVISION3}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex10-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex10-${REVISION2}.txt"
cp -f "${SCRIPT_DIR}/../data/annex10-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex10-${REVISION3}.txt"
cp -f "${SCRIPT_DIR}/../data/annex10-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex10-${REVISION2}.json"
cp -f "${SCRIPT_DIR}/../data/annex10-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex10-${REVISION3}.json"
cp -f "${SCRIPT_DIR}/../data/annex10-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex10-${REVISION2}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex10-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex10-${REVISION3}.pretty.json"

# Annex 13
echo "Processing annex 13..."
"${PYTHON}" "${SCRIPT_DIR}/budget2013_13.py" \
	-i "${SCRIPT_DIR}/../doc/annex13-${REVISION1}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex13-${REVISION1}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex13-${REVISION1}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex13-${REVISION1}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex13-${REVISION1}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex13-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex13-${REVISION2}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex13-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex13-${REVISION2}.txt"
cp -f "${SCRIPT_DIR}/../data/annex13-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex13-${REVISION2}.json"
cp -f "${SCRIPT_DIR}/../data/annex13-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex13-${REVISION2}.pretty.json"
"${PYTHON}" "${SCRIPT_DIR}/budget2013_13.py" \
	-i "${SCRIPT_DIR}/../doc/annex13-${REVISION3}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex13-${REVISION3}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex13-${REVISION3}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex13-${REVISION3}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex13-${REVISION3}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex13-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex13-combined-${REVISION1}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex13-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex13-combined-${REVISION1}.txt"
cp -f "${SCRIPT_DIR}/../data/annex13-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex13-combined-${REVISION1}.json"
cp -f "${SCRIPT_DIR}/../data/annex13-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex13-combined-${REVISION1}.pretty.json"

# Annex 13.1
echo "Processing annex 13.1..."
"${PYTHON}" "${SCRIPT_DIR}/budget2013_13_1.py" \
	-m "${SCRIPT_DIR}/../doc/annex13-${REVISION1}.txt" \
	-i "${SCRIPT_DIR}/../doc/annex13.1-${REVISION2}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex13.1-${REVISION2}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex13.1-${REVISION2}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex13.1-${REVISION2}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex13.1-${REVISION2}.pretty.json" \
	--combined-output-pickle "${SCRIPT_DIR}/../data/annex13-combined-${REVISION2}.pkl" \
	--combined-output-text "${SCRIPT_DIR}/../data/annex13-combined-${REVISION2}.txt" \
	--combined-output-json "${SCRIPT_DIR}/../data/annex13-combined-${REVISION2}.json" \
	--combined-output-json-pretty "${SCRIPT_DIR}/../data/annex13-combined-${REVISION2}.pretty.json"
"${PYTHON}" "${SCRIPT_DIR}/budget2013_13_1.py" \
	-m "${SCRIPT_DIR}/../doc/annex13-${REVISION3}.txt" \
	-i "${SCRIPT_DIR}/../doc/annex13.1-${REVISION2}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex13.1-${REVISION3}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex13.1-${REVISION3}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex13.1-${REVISION3}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex13.1-${REVISION3}.pretty.json" \
	--combined-output-pickle "${SCRIPT_DIR}/../data/annex13-combined-${REVISION3}.pkl.tmp"

# Annex 13.2
echo "Processing annex 13.2..."
"${PYTHON}" "${SCRIPT_DIR}/budget2013_13_2.py" \
	-m "${SCRIPT_DIR}/../data/annex13-combined-${REVISION3}.pkl.tmp" \
	-i "${SCRIPT_DIR}/../doc/annex13.2-${REVISION3}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex13.2-${REVISION3}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex13.2-${REVISION3}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex13.2-${REVISION3}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex13.2-${REVISION3}.pretty.json" \
	--combined-output-pickle "${SCRIPT_DIR}/../data/annex13-combined-${REVISION3}.pkl" \
	--combined-output-text "${SCRIPT_DIR}/../data/annex13-combined-${REVISION3}.txt" \
	--combined-output-json "${SCRIPT_DIR}/../data/annex13-combined-${REVISION3}.json" \
	--combined-output-json-pretty "${SCRIPT_DIR}/../data/annex13-combined-${REVISION3}.pretty.json"

rm -f "${SCRIPT_DIR}/../data/annex13-combined-${REVISION3}.pkl.tmp"

# Annex 15
echo "Processing annex 15..."
"${PYTHON}" "${SCRIPT_DIR}/budget2013_15.py" \
	-i "${SCRIPT_DIR}/../doc/annex15-${REVISION1}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex15-${REVISION1}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex15-${REVISION1}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex15-${REVISION1}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex15-${REVISION1}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex15-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex15-${REVISION2}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex15-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex15-${REVISION3}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex15-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex15-${REVISION2}.txt"
cp -f "${SCRIPT_DIR}/../data/annex15-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex15-${REVISION3}.txt"
cp -f "${SCRIPT_DIR}/../data/annex15-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex15-${REVISION2}.json"
cp -f "${SCRIPT_DIR}/../data/annex15-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex15-${REVISION3}.json"
cp -f "${SCRIPT_DIR}/../data/annex15-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex15-${REVISION2}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex15-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex15-${REVISION3}.pretty.json"

# Annex 19
echo "Processing annex 19..."
"${PYTHON}" "${SCRIPT_DIR}/budget2013_19.py" \
	-i "${SCRIPT_DIR}/../doc/annex19-${REVISION1}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex19-${REVISION1}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex19-${REVISION1}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex19-${REVISION1}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex19-${REVISION1}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex19-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex19-${REVISION2}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex19-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex19-${REVISION3}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex19-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex19-${REVISION2}.txt"
cp -f "${SCRIPT_DIR}/../data/annex19-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex19-${REVISION3}.txt"
cp -f "${SCRIPT_DIR}/../data/annex19-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex19-${REVISION2}.json"
cp -f "${SCRIPT_DIR}/../data/annex19-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex19-${REVISION3}.json"
cp -f "${SCRIPT_DIR}/../data/annex19-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex19-${REVISION2}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex19-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex19-${REVISION3}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex19-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex19-combined-${REVISION1}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex19-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex19-combined-${REVISION1}.txt"
cp -f "${SCRIPT_DIR}/../data/annex19-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex19-combined-${REVISION1}.json"
cp -f "${SCRIPT_DIR}/../data/annex19-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex19-combined-${REVISION1}.pretty.json"

# Annex 19.1
echo "Processing annex 19.1..."
"${PYTHON}" "${SCRIPT_DIR}/budget2013_19_1.py" \
	-m "${SCRIPT_DIR}/../doc/annex19-${REVISION1}.txt" \
	-i "${SCRIPT_DIR}/../doc/annex19.1-${REVISION2}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex19.1-${REVISION2}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex19.1-${REVISION2}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex19.1-${REVISION2}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex19.1-${REVISION2}.pretty.json" \
	--combined-output-pickle "${SCRIPT_DIR}/../data/annex19-combined-${REVISION2}.pkl" \
	--combined-output-text "${SCRIPT_DIR}/../data/annex19-combined-${REVISION2}.txt" \
	--combined-output-json "${SCRIPT_DIR}/../data/annex19-combined-${REVISION2}.json" \
	--combined-output-json-pretty "${SCRIPT_DIR}/../data/annex19-combined-${REVISION2}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex19.1-${REVISION2}.pkl" "${SCRIPT_DIR}/../data/annex19.1-${REVISION3}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex19.1-${REVISION2}.txt" "${SCRIPT_DIR}/../data/annex19.1-${REVISION3}.txt"
cp -f "${SCRIPT_DIR}/../data/annex19.1-${REVISION2}.json" "${SCRIPT_DIR}/../data/annex19.1-${REVISION3}.json"
cp -f "${SCRIPT_DIR}/../data/annex19.1-${REVISION2}.pretty.json" "${SCRIPT_DIR}/../data/annex19.1-${REVISION3}.pretty.json"

# Annex 19.2
echo "Processing annex 19.2..."
"${PYTHON}" "${SCRIPT_DIR}/budget2013_19_2.py" \
	-m "${SCRIPT_DIR}/../data/annex19-combined-${REVISION2}.pkl" \
	-i "${SCRIPT_DIR}/../doc/annex19.2-${REVISION3}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex19.2-${REVISION3}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex19.2-${REVISION3}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex19.2-${REVISION3}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex19.2-${REVISION3}.pretty.json" \
	--combined-output-pickle "${SCRIPT_DIR}/../data/annex19-combined-${REVISION3}.pkl" \
	--combined-output-text "${SCRIPT_DIR}/../data/annex19-combined-${REVISION3}.txt" \
	--combined-output-json "${SCRIPT_DIR}/../data/annex19-combined-${REVISION3}.json" \
	--combined-output-json-pretty "${SCRIPT_DIR}/../data/annex19-combined-${REVISION3}.pretty.json"

# Annex 22
echo "Processing annex 22..."
"${PYTHON}" "${SCRIPT_DIR}/budget2013_22.py" \
	-i "${SCRIPT_DIR}/../doc/annex22-${REVISION1}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex22-${REVISION1}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex22-${REVISION1}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex22-${REVISION1}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex22-${REVISION1}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex22-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex22-${REVISION2}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex22-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex22-${REVISION3}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex22-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex22-${REVISION2}.txt"
cp -f "${SCRIPT_DIR}/../data/annex22-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex22-${REVISION3}.txt"
cp -f "${SCRIPT_DIR}/../data/annex22-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex22-${REVISION2}.json"
cp -f "${SCRIPT_DIR}/../data/annex22-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex22-${REVISION3}.json"
cp -f "${SCRIPT_DIR}/../data/annex22-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex22-${REVISION2}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex22-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex22-${REVISION3}.pretty.json"

# Annex 25
echo "Processing annex 25..."
"${PYTHON}" "${SCRIPT_DIR}/budget2013_25.py" \
	-i "${SCRIPT_DIR}/../doc/annex25-${REVISION1}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex25-${REVISION1}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex25-${REVISION1}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex25-${REVISION1}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex25-${REVISION1}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex25-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex25-${REVISION2}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex25-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex25-${REVISION3}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex25-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex25-${REVISION2}.txt"
cp -f "${SCRIPT_DIR}/../data/annex25-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex25-${REVISION3}.txt"
cp -f "${SCRIPT_DIR}/../data/annex25-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex25-${REVISION2}.json"
cp -f "${SCRIPT_DIR}/../data/annex25-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex25-${REVISION3}.json"
cp -f "${SCRIPT_DIR}/../data/annex25-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex25-${REVISION2}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex25-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex25-${REVISION3}.pretty.json"

# Annex 26
echo "Processing annex 26..."
"${PYTHON}" "${SCRIPT_DIR}/budget2013_26.py" \
	-i "${SCRIPT_DIR}/../doc/annex26-${REVISION1}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex26-${REVISION1}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex26-${REVISION1}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex26-${REVISION1}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex26-${REVISION1}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex26-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex26-${REVISION2}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex26-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex26-${REVISION3}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex26-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex26-${REVISION2}.txt"
cp -f "${SCRIPT_DIR}/../data/annex26-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex26-${REVISION3}.txt"
cp -f "${SCRIPT_DIR}/../data/annex26-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex26-${REVISION2}.json"
cp -f "${SCRIPT_DIR}/../data/annex26-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex26-${REVISION3}.json"
cp -f "${SCRIPT_DIR}/../data/annex26-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex26-${REVISION2}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex26-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex26-${REVISION3}.pretty.json"

# Annex 31
echo "Processing annex 31..."
"${PYTHON}" "${SCRIPT_DIR}/budget2013_31.py" \
	-i "${SCRIPT_DIR}/../doc/annex31-${REVISION1}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex31-${REVISION1}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex31-${REVISION1}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex31-${REVISION1}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex31-${REVISION1}.pretty.json"
"${PYTHON}" "${SCRIPT_DIR}/budget2013_31.py" \
	-i "${SCRIPT_DIR}/../doc/annex31-${REVISION2}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex31-${REVISION2}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex31-${REVISION2}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex31-${REVISION2}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex31-${REVISION2}.pretty.json"
"${PYTHON}" "${SCRIPT_DIR}/budget2013_31.py" \
	-i "${SCRIPT_DIR}/../doc/annex31-${REVISION3}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex31-${REVISION3}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex31-${REVISION3}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex31-${REVISION3}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex31-${REVISION3}.pretty.json"

# Annex 32
echo "Processing annex 32..."
"${PYTHON}" "${SCRIPT_DIR}/budget2013_32.py" \
	-i "${SCRIPT_DIR}/../doc/annex32-${REVISION1}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex32-${REVISION1}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex32-${REVISION1}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex32-${REVISION1}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex32-${REVISION1}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex32-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex32-${REVISION2}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex32-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex32-${REVISION3}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex32-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex32-${REVISION2}.txt"
cp -f "${SCRIPT_DIR}/../data/annex32-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex32-${REVISION3}.txt"
cp -f "${SCRIPT_DIR}/../data/annex32-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex32-${REVISION2}.json"
cp -f "${SCRIPT_DIR}/../data/annex32-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex32-${REVISION3}.json"
cp -f "${SCRIPT_DIR}/../data/annex32-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex32-${REVISION2}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex32-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex32-${REVISION3}.pretty.json"

# Annex 35
echo "Processing annex 35..."
"${PYTHON}" "${SCRIPT_DIR}/budget2013_35.py" \
	-i "${SCRIPT_DIR}/../doc/annex35-${REVISION1}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex35-${REVISION1}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex35-${REVISION1}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex35-${REVISION1}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex35-${REVISION1}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex35-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex35-${REVISION2}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex35-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex35-${REVISION2}.txt"
cp -f "${SCRIPT_DIR}/../data/annex35-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex35-${REVISION2}.json"
cp -f "${SCRIPT_DIR}/../data/annex35-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex35-${REVISION2}.pretty.json"
"${PYTHON}" "${SCRIPT_DIR}/budget2013_35.py" \
	-i "${SCRIPT_DIR}/../doc/annex35-${REVISION3}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex35-${REVISION3}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex35-${REVISION3}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex35-${REVISION3}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex35-${REVISION3}.pretty.json"

# Annex 36
echo "Processing annex 36..."
"${PYTHON}" "${SCRIPT_DIR}/budget2013_36.py" \
	-i "${SCRIPT_DIR}/../doc/annex36-${REVISION1}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex36-${REVISION1}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex36-${REVISION1}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex36-${REVISION1}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex36-${REVISION1}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex36-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex36-${REVISION2}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex36-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex36-${REVISION3}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex36-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex36-${REVISION2}.txt"
cp -f "${SCRIPT_DIR}/../data/annex36-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex36-${REVISION3}.txt"
cp -f "${SCRIPT_DIR}/../data/annex36-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex36-${REVISION2}.json"
cp -f "${SCRIPT_DIR}/../data/annex36-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex36-${REVISION3}.json"
cp -f "${SCRIPT_DIR}/../data/annex36-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex36-${REVISION2}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex36-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex36-${REVISION3}.pretty.json"

# Annex 37
echo "Processing annex 37..."
"${PYTHON}" "${SCRIPT_DIR}/budget2013_37.py" \
	-i "${SCRIPT_DIR}/../doc/annex37-${REVISION1}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex37-${REVISION1}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex37-${REVISION1}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex37-${REVISION1}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex37-${REVISION1}.pretty.json"
"${PYTHON}" "${SCRIPT_DIR}/budget2013_37.py" \
	-i "${SCRIPT_DIR}/../doc/annex37-${REVISION2}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex37-${REVISION2}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex37-${REVISION2}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex37-${REVISION2}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex37-${REVISION2}.pretty.json"
"${PYTHON}" "${SCRIPT_DIR}/budget2013_37.py" \
	-i "${SCRIPT_DIR}/../doc/annex37-${REVISION3}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex37-${REVISION3}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex37-${REVISION3}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex37-${REVISION3}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex37-${REVISION3}.pretty.json"

# Annex 38
echo "Processing annex 38..."
"${PYTHON}" "${SCRIPT_DIR}/budget2013_38.py" \
	-i "${SCRIPT_DIR}/../doc/annex38-${REVISION1}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex38-${REVISION1}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex38-${REVISION1}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex38-${REVISION1}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex38-${REVISION1}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex38-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex38-${REVISION2}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex38-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex38-${REVISION3}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex38-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex38-${REVISION2}.txt"
cp -f "${SCRIPT_DIR}/../data/annex38-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex38-${REVISION3}.txt"
cp -f "${SCRIPT_DIR}/../data/annex38-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex38-${REVISION2}.json"
cp -f "${SCRIPT_DIR}/../data/annex38-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex38-${REVISION3}.json"
cp -f "${SCRIPT_DIR}/../data/annex38-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex38-${REVISION2}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex38-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex38-${REVISION3}.pretty.json"

# Annex 39
echo "Processing annex 39..."
"${PYTHON}" "${SCRIPT_DIR}/budget2013_39.py" \
	-i "${SCRIPT_DIR}/../doc/annex39-${REVISION1}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex39-${REVISION1}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex39-${REVISION1}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex39-${REVISION1}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex39-${REVISION1}.pretty.json"
"${PYTHON}" "${SCRIPT_DIR}/budget2013_39.py" \
	-i "${SCRIPT_DIR}/../doc/annex39-${REVISION2}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex39-${REVISION2}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex39-${REVISION2}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex39-${REVISION2}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex39-${REVISION2}.pretty.json"
"${PYTHON}" "${SCRIPT_DIR}/budget2013_39.py" \
	-i "${SCRIPT_DIR}/../doc/annex39-${REVISION3}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex39-${REVISION3}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex39-${REVISION3}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex39-${REVISION3}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex39-${REVISION3}.pretty.json"

# Annex 40
echo "Processing annex 40..."
"${PYTHON}" "${SCRIPT_DIR}/budget2013_40.py" \
	-i "${SCRIPT_DIR}/../doc/annex40-${REVISION1}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex40-${REVISION1}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex40-${REVISION1}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex40-${REVISION1}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex40-${REVISION1}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex40-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex40-${REVISION2}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex40-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex40-${REVISION3}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex40-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex40-${REVISION2}.txt"
cp -f "${SCRIPT_DIR}/../data/annex40-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex40-${REVISION3}.txt"
cp -f "${SCRIPT_DIR}/../data/annex40-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex40-${REVISION2}.json"
cp -f "${SCRIPT_DIR}/../data/annex40-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex40-${REVISION3}.json"
cp -f "${SCRIPT_DIR}/../data/annex40-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex40-${REVISION2}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex40-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex40-${REVISION3}.pretty.json"

# Annex 41
echo "Processing annex 41..."
"${PYTHON}" "${SCRIPT_DIR}/budget2013_41.py" \
	-i "${SCRIPT_DIR}/../doc/annex41-${REVISION1}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex41-${REVISION1}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex41-${REVISION1}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex41-${REVISION1}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex41-${REVISION1}.pretty.json"
"${PYTHON}" "${SCRIPT_DIR}/budget2013_41.py" \
	-i "${SCRIPT_DIR}/../doc/annex41-${REVISION2}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex41-${REVISION2}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex41-${REVISION2}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex41-${REVISION2}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex41-${REVISION2}.pretty.json"
"${PYTHON}" "${SCRIPT_DIR}/budget2013_41.py" \
	-i "${SCRIPT_DIR}/../doc/annex41-${REVISION3}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex41-${REVISION3}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex41-${REVISION3}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex41-${REVISION3}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex41-${REVISION3}.pretty.json"

# Annex 42
echo "Processing annex 42..."
"${PYTHON}" "${SCRIPT_DIR}/budget2013_42.py" \
	-i "${SCRIPT_DIR}/../doc/annex42-${REVISION1}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex42-${REVISION1}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex42-${REVISION1}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex42-${REVISION1}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex42-${REVISION1}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex42-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex42-${REVISION2}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex42-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex42-${REVISION3}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex42-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex42-${REVISION2}.txt"
cp -f "${SCRIPT_DIR}/../data/annex42-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex42-${REVISION3}.txt"
cp -f "${SCRIPT_DIR}/../data/annex42-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex42-${REVISION2}.json"
cp -f "${SCRIPT_DIR}/../data/annex42-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex42-${REVISION3}.json"
cp -f "${SCRIPT_DIR}/../data/annex42-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex42-${REVISION2}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex42-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex42-${REVISION3}.pretty.json"

# Annex 43
echo "Processing annex 43..."
"${PYTHON}" "${SCRIPT_DIR}/budget2013_43.py" \
	-i "${SCRIPT_DIR}/../doc/annex43-${REVISION1}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex43-${REVISION1}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex43-${REVISION1}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex43-${REVISION1}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex43-${REVISION1}.pretty.json"
"${PYTHON}" "${SCRIPT_DIR}/budget2013_43.py" \
	-i "${SCRIPT_DIR}/../doc/annex43-${REVISION2}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex43-${REVISION2}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex43-${REVISION2}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex43-${REVISION2}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex43-${REVISION2}.pretty.json"
"${PYTHON}" "${SCRIPT_DIR}/budget2013_43.py" \
	-i "${SCRIPT_DIR}/../doc/annex43-${REVISION3}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex43-${REVISION3}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex43-${REVISION3}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex43-${REVISION3}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex43-${REVISION3}.pretty.json"

# Annex 44
echo "Processing annex 44..."
"${PYTHON}" "${SCRIPT_DIR}/budget2013_44.py" \
	-i "${SCRIPT_DIR}/../doc/annex44-${REVISION1}.txt" \
	--output-pickle "${SCRIPT_DIR}/../data/annex44-${REVISION1}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/annex44-${REVISION1}.txt" \
	--output-json "${SCRIPT_DIR}/../data/annex44-${REVISION1}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/annex44-${REVISION1}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex44-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex44-${REVISION2}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex44-${REVISION1}.pkl" "${SCRIPT_DIR}/../data/annex44-${REVISION3}.pkl"
cp -f "${SCRIPT_DIR}/../data/annex44-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex44-${REVISION2}.txt"
cp -f "${SCRIPT_DIR}/../data/annex44-${REVISION1}.txt" "${SCRIPT_DIR}/../data/annex44-${REVISION3}.txt"
cp -f "${SCRIPT_DIR}/../data/annex44-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex44-${REVISION2}.json"
cp -f "${SCRIPT_DIR}/../data/annex44-${REVISION1}.json" "${SCRIPT_DIR}/../data/annex44-${REVISION3}.json"
cp -f "${SCRIPT_DIR}/../data/annex44-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex44-${REVISION2}.pretty.json"
cp -f "${SCRIPT_DIR}/../data/annex44-${REVISION1}.pretty.json" "${SCRIPT_DIR}/../data/annex44-${REVISION3}.pretty.json"

# Result budget
echo "Processing result budget..."
"${PYTHON}" "${SCRIPT_DIR}/budget2013_result.py" \
	-i "${SCRIPT_DIR}/../data" \
	-r "${REVISION1}" \
	--output-pickle "${SCRIPT_DIR}/../data/result-${REVISION1}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/result-${REVISION1}.txt" \
	--output-json "${SCRIPT_DIR}/../data/result-${REVISION1}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/result-${REVISION1}.pretty.json"
"${PYTHON}" "${SCRIPT_DIR}/budget2013_result.py" \
	-i "${SCRIPT_DIR}/../data" \
	-r "${REVISION2}" \
	--output-pickle "${SCRIPT_DIR}/../data/result-${REVISION2}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/result-${REVISION2}.txt" \
	--output-json "${SCRIPT_DIR}/../data/result-${REVISION2}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/result-${REVISION2}.pretty.json"
"${PYTHON}" "${SCRIPT_DIR}/budget2013_result.py" \
	-i "${SCRIPT_DIR}/../data" \
	-r "${REVISION3}" \
	--output-pickle "${SCRIPT_DIR}/../data/result-${REVISION3}.pkl" \
	--output-text "${SCRIPT_DIR}/../data/result-${REVISION3}.txt" \
	--output-json "${SCRIPT_DIR}/../data/result-${REVISION3}.json" \
	--output-json-pretty "${SCRIPT_DIR}/../data/result-${REVISION3}.pretty.json"

echo "Processing completed."
