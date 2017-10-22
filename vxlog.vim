" Vim syntax file
"


syn case match

syn match   i75		/DEBUG.*/
hi	i75		ctermfg=white ctermbg=darkblue

syn match   i7		/DEBUG.\{-}>.\{-}bolt\d\+:.\{-}vxcli\_.\{-}result\_.\{-}\[\d\{4}.\{-}\]/
hi	i7		ctermfg=magenta

syn match   i71		/.\{-}packets transmitted.\{-}packet loss.*/
hi	i71		ctermfg=white ctermbg=darkblue

syn match   i72		/INFO:\s\+\w.*/
hi	i72		ctermfg=black ctermbg=darkgreen

syn match   i73		/WARNING.*/
hi	i73		ctermfg=white ctermbg=darkyellow

syn match   i74		/ERROR.*/
hi	i74		ctermfg=white ctermbg=darkred


syn match   i4		/DEBUG.\{-}>.\{-}bolt\d\+-.\{-}vx\_.\{-}result\_.\{-}\[\d\{4}.\{-}\]/
hi	i4		ctermfg=yellow

syn match   i5		/DEBUG.\{-}>.\{-}bolt\d\+:.\{-}vxcli\s\{-}sa\_.\{-}result\_.\{-}\[\d\{4}.\{-}\]/
hi	i5		ctermfg=red

syn match   i51		/DEBUG.\{-}>.\{-}bolt\d\+:.\{-}vxcli\s\{-}ig\_.\{-}result\_.\{-}\[\d\{4}.\{-}\]/
hi	i51		ctermfg=lightgreen

syn match   i52		/DEBUG.\{-}>.\{-}bolt\d\+:.\{-}vxcli\s\{-}eg\_.\{-}result\_.\{-}\[\d\{4}.\{-}\]/
hi	i52		ctermfg=lightcyan

syn match   i6		/DEBUG.\{-}>.\{-}bolt\d\+:.\{-}vxcli\s\{-}volume\_.\{-}result\_.\{-}\[\d\{4}.\{-}\]/
hi	i6		ctermfg=cyan

syn match   i61		/DEBUG.\{-}>.\{-}bolt\d\+:.\{-}vxcli\s\{-}dg\_.\{-}result\_.\{-}\[\d\{4}.\{-}\]/
hi	i61		ctermfg=lightblue

syn match   ignore1		/INFO.*esm dbg\_.\{-}result\_.\{-}\[\d\{4}.\{-}\]/

syn match   i8		/DEBUG.\{-}execute..maim.\{-}\_.\{-}result\_.\{-}\[\d\{4}.\{-}\]/
hi	i8		ctermfg=black ctermbg=red

syn match   ignore1		/DEBUG.*multi\_.\{-}result\_.\{-}\[\d\{4}.\{-}\]/
syn match   ignore1		/DEBUG.*set +m\_.\{-}result\_.\{-}\[\d\{4}.\{-}\]/
syn match   ignore1		/DEBUG.\{-}>.\{-}df -h\_.\{-}result\_.\{-}\[\d\{4}.\{-}\]/
syn match   ignore1		/INFO.*sg_inq\_.\{-}result\_.\{-}\[\d\{4}.\{-}\]/
syn match   ignore1		/DEBUG.*lspci\_.\{-}result\_.\{-}\[\d\{4}.\{-}\]/
syn match   ignore1		/DEBUG.*mount\_.\{-}result\_.\{-}\[\d\{4}.\{-}\]/
syn match   ignore1		/DEBUG.*cd -\_.\{-}result\_.\{-}\[\d\{4}.\{-}\]/
syn match   ignore1		/DEBUG.*cd \/tmp\_.\{-}result\_.\{-}\[\d\{4}.\{-}\]/
syn match   ignore1		/DEBUG.*export\_.\{-}result\_.\{-}\[\d\{4}.\{-}\]/
syn match   ignore1		/DEBUG.*dmesg\_.\{-}result\_.\{-}\[\d\{4}.\{-}\]/
syn match   ignore1		/INFO.*mkdir\_.\{-}result\_.\{-}\[\d\{4}.\{-}\]/
syn match   ignore1		/DEBUG.*blockdev\_.\{-}result\_.\{-}\[\d\{4}.\{-}\]/
syn match   ignore1		/INFO.*which qaucli\_.\{-}result\_.\{-}\[\d\{4}.\{-}\]/
syn match   ignore1		/INFO.*tar \_.\{-}result\_.\{-}\[\d\{4}.\{-}\]/
syn match   ignore1		/INFO.*scp \_.\{-}result\_.\{-}\[\d\{4}.\{-}\]/
syn match   ignore1		/INFO.*ssh -q\_.\{-}result\_.\{-}\[\d\{4}.\{-}\]/
syn match   ignore1		/INFO.*rm -f\_.\{-}result\_.\{-}\[\d\{4}.\{-}\]/
syn match   ignore1		/DEBUG.*bolt\d\+.\{-}vxstats\_.\{-}result\_.\{-}\[\d\{4}.\{-}\]/
syn match   ignore1		/DEBUG.\{-}sys\/class\_.\{-}result\_.\{-}\[\d\{4}.\{-}\]/
hi	ignore1		ctermfg=darkGrey 
"hi	ignore1		ctermfg=black

syn match   i9		/.\{-}STARTING.*/
hi	i9		ctermfg=white ctermbg=red

syn match   i10		/.\{-}FINISH.*/
hi	i10		ctermfg=white ctermbg=red

syn match   i11		/.\{-}OUTCOME.*/
hi	i11		ctermfg=white ctermbg=red
