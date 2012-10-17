#!/bin/bash
echo "Yes instances:"
for f in Yes/*.in; do echo "Processing $f file.."; $1 <$f; done
echo "No instances:"
for f in No/*.in; do echo "Processing $f file.."; $1 <$f; done


