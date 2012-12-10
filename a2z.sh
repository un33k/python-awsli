#!/usr/bin/env bash

CMD_HOME="`pwd`/awsli/commands"
USAGE="Usage: a2z [-l|ls|list|-h|help] <command> [options]"
function a2z {
    argv=($@)
    opts=()
    args=()
    parse_cmd=0
    for a in ${argv[*]}
    do
        if [ $parse_cmd -eq 0 ]
        then
            cmd="$CMD_HOME/$a"
            cmdpy="$CMD_HOME/$a.py"
            cmdsh="$CMD_HOME/$a.sh"
        
            if [ -e $cmd ]
                then
                    args+=$cmd
                    parse_cmd=1
                continue
            elif [ -e $cmdpy ]
                then
                    args+=$cmdpy
                    parse_cmd=1
                continue
            elif [ -e $cmdsh ]
                then
                    args+=$cmdsh
                    parse_cmd=1
                continue
            fi
            opts+=($a)
        else
            args+=($a)
        fi
    done
    #echo "OPTS: ${opts[*]}"
    #echo "ARGS: ${args[*]}"
    for o in ${opts[*]}
    do
        if [ "$o" == "-l" ] || [ "$o" == "ls" ] || [ "$o" == "list" ]
        then
            ls=($(compgen -X "*__*" -W "`ls $CMD_HOME`" -- ))
            len=${#ls[$i]}
            ls[$i]=${ls[$i]:0:$len-3}
            echo ${ls[*]}
            return 0
        elif [ "$o" == "-h" ] || [ "$o" == "help" ]
        #Invoke individual command help
        then
            if [ ${#args} -gt 0 ]
            then
                out="`python ${args[0]} -h`"
                echo "$out"
                return 0
            fi
            echo "$USAGE"
            return 0
        else
            echo "$USAGE"
            return 0
        fi
    done
    if [ $parse_cmd -eq 1 ]
    then
        out="`python ${args[@]}`"
        echo "$out"
        return 0
    fi
    echo "$USAGE"
    return 0
}

function _complete_()
{
    local word=${COMP_WORDS[COMP_CWORD]}
    local xpat='*__*'
    
    COMPREPLY=($(compgen -X "$xpat" -W "`ls $CMD_HOME`" -- ${word}))
 
    for i in ${!COMPREPLY[*]}
    do
        #strip .py
        len=${#COMPREPLY[$i]}
        COMPREPLY[$i]=${COMPREPLY[$i]:0:$len-3}
    done
}
complete -F _complete_ a2z
