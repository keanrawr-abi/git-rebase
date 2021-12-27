# git Rebase

When you have a merge conflict but don't necessarily want to choose one of the conflicting version over the other, but rather applying the conflicting changes to your files, `git rebase` is the solution to your problem.

## What does it mean to rebase?

When you create a branch, the source of your branch might get changes applied during your work on your separate branch. Some times you'll want to apply those new changes to your current branch, that is called rebasing.

Imagine the following situation: you've created a branch based on the `main` branch and implemented some feature, whilst your work was being done, some changes have been commited to `main`. The commit graph would look something like this:

```
      A---B---C feature
     /
D---E---F---G main
```

To do a rebase you'd have to do something like:

```bash
# git rebase <source> <target>
git rebase main feature
```

Doing this would change the commit graph to this:

```
              A'--B'--C' feature
             /
D---E---F---G main
```

Note that the `F` and `G` commits have been applied to the `feature` branch. However, `A` and `A'` are different commits.

Congrats! you've rebases a branch! 🎉

### What happened?

What git has basically done is:

1. Calculate wich changes have been commited to `main` that aren't present in `feature` (`F` and `G` in our case)
2. Undo the commits made in `feature` (time travel to the point where `main` and `feature` diverge)
3. Apply the changes in `A`, `B` and `C` as new different commits

### merge conflicts

During step 3 there might be some merge conflicts that will need to be solved, use your knowledge of merge conflicts to get around those.

The workflow is normally the following.

1. git will let you know that during the rebase there's a merge conflict and pause the rebase
2. solve the merge conflict
3. commit the merge conflict resolution
4. use `git rebase --continue` to resume the rebase

For branches that have diverged for a lot of commits, this process might need to be applied several times.
