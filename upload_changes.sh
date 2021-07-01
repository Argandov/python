echo "To be commited: "
git status
git add -A
echo "Commit messg?"
read messg
git commit -m $messg
git status
