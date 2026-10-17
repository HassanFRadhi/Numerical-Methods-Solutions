function Minv = Matrix_Inverse_Solve(A,b)
    [m,n] = size(A);
    if m ~= n
        error('Matrix Must Be Squared')
    end
    AugM=[A eye(n)];

    % Partial Pivoting
    for i = 1:n
        [~,max_row] = max(abs(AugM(i:end,i)));
        max_row = max_row + i - 1;

        % Checking non-singularity
        if AugM(max_row,i) == 0
            error('Matrix Is Singular')
        end
        if max_row ~= i
            AugM([i,max_row],:) = AugM([max_row, i],:);
        end

       % Calculating The inverse matrix
       AugM(i,:) = AugM(i,:)/AugM(i,i);
       for j = 1:n
           if j ~= i
               AugM(j,:) = AugM(j,:) - AugM(j,i)*AugM(i,:);
           end
       end

    end
    invA = AugM(:,n+1:end);
    X = invA * b;
    display(X)
